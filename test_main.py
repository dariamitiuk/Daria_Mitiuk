from main import Cloud_Storage

ACCESS_TOKEN = 'sl.BWhBbCr-6SkL7A0XsTBY5uFlrcXU8EPOwH63PzmBJ68hbRBnMwBth-rDDin1AD_uAHSpjdQ0qQOmzOHfmENPOd3dUxgJ9P35tijKQK0XXkjWIfS-Ov54yyrWbhNb760jMc6BoY9JWJOa'
file = 'filename.txt'
path = '/test/filename.txt'
user = Cloud_Storage(ACCESS_TOKEN)

def test_uploadFile():
    assert user.uploadFile(file, path) == 1

def test_getMetadata():
    assert user.getMetadata(path) == 1

def test_deleteFile():
    assert user.deleteFile(path) == 1
