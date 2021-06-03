import pathlib
import os

from .gdrive import uploadPDF
from . import logging

log = logging.getLogger(__name__)

dirName = 'pdf'
try:
    # Create target Directory
    os.mkdir(dirName)
    print("Directory ", dirName, " Created ")
except FileExistsError:
    print("Directory ", dirName, " already exists")


def download_file(ses, url, filename):
    if not os.path.exists('pdf/' + filename + '.pdf'):
        log.info("downloading %s ...", filename)
        response = ses.get(url)
        file = open('pdf/' + filename + ".pdf", 'wb')
        file.write(response.content)
        file.close()
    path = str(pathlib.Path().absolute()) + f'/pdf/{filename}.pdf'
    #file_path = '/'.join(path.split("\\"))
    log.info("uploading %s ...", filename)
    link = uploadPDF(path, filename)
    return {"path": link}
