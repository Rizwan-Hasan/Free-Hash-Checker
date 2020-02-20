# /run/media/rizwan/Video/Movies/Robin.Hood.2018.1080p.WEB-DL.DD5.1.H264-FGT.mkv
# /run/media/rizwan/Softwares/Games/MathWorks Matlab R2018a.iso

from hashlib import md5, sha256, sha512
from os import stat

from tqdm import tqdm


def checkHash(fileLoc, option):
    # Specifying how many bytes of the file to open at a time ↓
    BLOCKSIZE = 4096
    # 4096 Byte = 4 KiloByte

    # Variables  ↓
    count: int = 0
    sizeCount = 0
    MB: float = 0.000001
    fileSize = stat(fileLoc).st_size
    perUnit = fileSize / 100
    print(perUnit)
    md5Hasher = md5()
    sha256Hasher = sha256()
    sha512Hasher = sha512()

    # Desired hashing ↓
    with open(fileLoc, 'rb') as file:
        fileData = file.read(BLOCKSIZE)
        progressBar = tqdm(total=100)
        if option == 'md5':  # MD5sum ↓
            while fileData:
                sizeCount += BLOCKSIZE
                if sizeCount >= perUnit:
                    sizeCount -= perUnit
                    count += 1
                    # print(count)
                    progressBar.update(1)
                md5Hasher.update(fileData)
                fileData = file.read(BLOCKSIZE)
            else:
                count = 100
                # print(count)
                progressBar.update(count)
                progressBar.close()
            return md5Hasher.hexdigest()

        elif option == 'sha256':  # SHA256sum ↓
            while fileData:
                sizeCount += BLOCKSIZE
                if sizeCount >= perUnit:
                    sizeCount -= perUnit
                    count += 1
                    # print(count)
                    progressBar.update(1)
                sha256Hasher.update(fileData)
                fileData = file.read(BLOCKSIZE)
            else:
                count = 100
                # print(count)
                progressBar.update(count)
                progressBar.close()
            return sha256Hasher.hexdigest()

        elif option == 'sha512':  # SHA512sum ↓
            while fileData:
                sizeCount += BLOCKSIZE
                if sizeCount >= perUnit:
                    sizeCount -= perUnit
                    count += 1
                    # print(count)
                    progressBar.update(1)
                sha512Hasher.update(fileData)
                fileData = file.read(BLOCKSIZE)
            else:
                count = 100
                # print(count)
                progressBar.update(count)
                progressBar.close()
            return sha512Hasher.hexdigest()

        else:
            return -1


if __name__ == '__main__':
    fileName: str = '/run/media/rizwan/Softwares/Games/MathWorks Matlab R2018a.iso'
    hashType: str = 'sha512'
    fileHash = checkHash(fileName, hashType)
    print(fileHash)
