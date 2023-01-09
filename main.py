import dropbox

class Cloud_Storage:
    def __init__(self, access_token):
        self.tkn = access_token
    def uploadFile(self, file_from, file_to):
        f = open(file_from, 'rb')
        f = f.read()
        dbx = dropbox.Dropbox(self.tkn)
        if file_from != '' and file_to != '':
            dbx.files_upload(f, file_to)
            return 1
        else:
            return 0

    def deleteFile(self, path):
        dbx = dropbox.Dropbox(self.tkn)
        dbx.files_delete_v2(path)
        return 1

    def getMetadata(self, path):
        dbx = dropbox.Dropbox(self.tkn)
        res = dbx.files_get_metadata(path)
        return 1

