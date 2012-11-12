from facepy import GraphAPI, FacepyError 
import os.path
import urllib2
import re

class Photo:
    def __init__(self, directory):
        self.directory = directory

        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

    def download(self, url, subdir=''):
        print " %s..." % (url),

        # Grab filename from path
        filename = re.search(r"""[^/]+$""", str(url)).group(0)

        try:
            req = urllib2.Request(url)
            response = urllib2.urlopen(req)
        except urllib2.URLError, e:
            print " can't grab image"
            return

        if subdir != '':
            album_dir = self.directory + subdir
            if not os.path.exists(album_dir):
                os.makedirs(album_dir)
        else:
            album_dir = self.directory

        filepath =  album_dir + '/' + filename
        if not os.path.isfile(filepath):
            output = open(filepath, 'wb')
            output.write(response.read())
            output.close()

        print " done"


class FacebookPhoto(object):
    def __init__(self, access_token):
        self.access_token = access_token
        self.graph = GraphAPI(self.access_token)

    def photos(self):
        query = {'query': 'SELECT object_id, pid, aid, images, caption, position FROM photo WHERE owner=me() or pid in (SELECT pid FROM photo_tag WHERE subject=me()) LIMIT 1500'}
        return self._fql_result(self.graph.fql(query))

    def album(self, aid):
        query = {'query': 'SELECT object_id, type, owner, name, description, size, link, photo_count FROM album WHERE aid='+aid}
        return self._fql_result(self.graph.fql(query))

    def album_user(self, userid):
        query = {'query': 'SELECT name FROM user WHERE uid = "'+str(userid)+'"'}
        return self._fql_result(self.graph.fql(query))

    def album_photos(self, aid):
        query = {'query': 'SELECT object_id, pid, aid, images, caption, position FROM photo WHERE aid="'+ aid +'" LIMIT 1000'}
        return self._fql_result(self.graph.fql(query))

    def albums(self):
        print "Getting your tagged photos albums..."

        albums = set()
        for photo in self.photos():
            albums.add(photo['aid'])

        results = []
        i = 1
        num_albums = len(albums)
        for aid in albums:
            print "\t(%d, %d) grabbing album id %s" % (i, num_albums, aid)
            album_data = {'data': {}, 'photos': {}}
            try:
                album = self.album(aid)
                if album != []:
                    album_data['data'] = album[0]
                    userid = album_data['data']['owner']
                    album_data['user'] = self.album_user(userid)[0]
                    album_data['data']['name'] = self._augment_album_name(album_data['data']['name'], album_data['user']['name'])
                    album_data['photos'] = self.album_photos(aid)
                    results.append(album_data)

            except FacepyError as e:
                print "Error Retreiving album_id: %s" % aid

            i += 1

            
        return results

    def _augment_album_name(self, album_name, augment):
        if album_name == 'Mobile Uploads':
            album_name = augment + ' Mobile Uploads'
        elif album_name == 'Profile Pictures':
            album_name = augment + ' Profile Pictures'
        else:
            album_name += ' (' + augment + ')'

        return album_name

    def _fql_result(self, result):
        return result['data'][0]['fql_result_set']

if __name__ == '__main__':
    access_token = "ACCESS_CODE_HERE"
    base_dir = '/Users/tasp/Dropbox/Personal/Photos/Facebook/'
    tagged_dir = '_TaggedPhotos'

    f = FacebookPhoto(access_token)

    print "Grabbing your tagged photos"
    photos = f.photos()

    num_photos = len(photos)
    print "\t# Photos: %d" % num_photos
    i = 0
    for p in photos:
        photo = Photo(base_dir)
        img_url = p['images'][0]['source']
        print "(%d/%d) " % (i, num_photos),
        photo.download(img_url, tagged_dir)
        i += 1

    albums = f.albums()

    num_albums = len(albums)
    print "Number of albums: %d" % num_albums
    print "Starting album downloads..."
    print "#"*20
    for album in albums:
        album_name = album['data']['name']
        num_album_photos = len(album['photos'])

        print "Downloading %s" % album_name 
        print "\t# Photos: %d" % num_album_photos
        i = 1
        for img in album['photos']:
            photo = Photo(base_dir)
            img_url = img['images'][0]['source']
            print "(%d/%d) " % (i, num_album_photos),
            photo.download(img_url, album_name)
            i += 1


        print "And we're done."

