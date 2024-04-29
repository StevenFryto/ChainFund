import sys
sys.path.append("d:\\CyberSecurity\\me\\JiShe\\4.0\\ChainFund")

from fisco_bcos.python_sdk.client.bcosclient import BcosClient
from fisco_bcos.python_sdk.client.datatype_parser import DatatypeParser
# from fisco_bcos.python_sdk.eth_utils import to_checksum_address, keccak, decode_hex,encode_hex


# 创建client对象
client = BcosClient()
print(client.getinfo())

# 定义智能合约地址及abi
to_address = "0xf2818ae69ef667d120584b981a818b982cd6d7f5"
contractFile = "./blockchain/contracts/ChainFund_2.abi"
abi_parser = DatatypeParser()
abi_parser.load_abi_file(contractFile)
contract_abi = abi_parser.contract_abi


# 插入资金流动记录
def insertRecord(args : list):
    result = client.sendRawTransactionGetReceipt(to_address, contract_abi, fn_name="insertRecord", args=args)
    print(result)
    # return result['blockHash']
    return result


# 通过获取 <捐钱者id> 资金流动记录
def getRecordsByFromUser(args : list):
    return client.call(to_address, contract_abi, fn_name="getRecordsByFromUser", args=args)


# 通过获取 <发起者id> 资金流动记录
def getRecordsByToUser(args : list):
    return client.call(to_address, contract_abi, fn_name="getRecordsByToUser", args=args)


# 通过获取 <项目id> 资金流动记录
def getRecordsByProjectId(args : list):
    return client.call(to_address, contract_abi, fn_name="getRecordsByProjectId", args=args)
