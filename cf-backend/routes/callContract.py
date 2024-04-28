import sys
sys.path.append("d:\\CyberSecurity\\me\\JiShe\\4.0\\ChainFund")

from blockchain import chainfund


if __name__ == '__main__':
    # block_hash = chainfund.insertRecord(args=[14, 1, 1, 20000, "家人们谁懂啊"])
    # print(block_hash)
    # results = chainfund.getRecordsByFromUser(args=[1])
    # results = chainfund.getRecordsByToUser(args=[14])
    results = chainfund.getRecordsByProjectId(args=[1])
    print(results[0])
    
    # 输出：((1, 1, 14, 1, 2000, '芝士雪豹', 1714213084123), (2, 2, 14, 1, 5000, '我测你嘛', 1714213152937), (4, 14, 1, 1, 20000, '轻舟已过万重山❤', 1714237752539))