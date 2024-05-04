import sys
sys.path.append("d:\\CyberSecurity\\me\\JiShe\\4.0\\ChainFund")

from blockchain import chainfund


if __name__ == '__main__':
    # block_hash = chainfund.insertRecord(args=[14, 1, 1, 20000, "祝你早日康复"])
    # print(block_hash)
    # results = chainfund.getRecordsByFromUser(args=[1])
    # results = chainfund.getRecordsByToUser(args=[14])
    results = chainfund.getRecordsByProjectId(args=[1])
