pragma solidity ^0.6.10;
pragma experimental ABIEncoderV2;

contract ChainFund_2 {
    struct Record {
        uint256 fundId;
        uint256 fromUser;
        uint256 toUser;
        uint256 projectId;
        uint256 fundValue;
        string message;
        uint256 time;
    }
    
    uint256 public currentFundId;
    mapping(uint256 => Record) public records;
    
    constructor() public {
        currentFundId = 1;
    }
    
    function insertRecord(uint256 _fromUser, uint256 _toUser, uint256 _projectId, uint256 _fundValue, string memory _message) 
    public 
    returns(uint256) {
        uint256 fundId = currentFundId;
        records[fundId] = Record(fundId, _fromUser, _toUser, _projectId, _fundValue, _message, block.timestamp);
        currentFundId++;
        return fundId;
    }
    
    function getRecordById(uint256 _fundId) public view returns(uint256, uint256, uint256, uint256, uint256, string memory, uint256) {
        Record memory record = records[_fundId];
        return (record.fundId, record.fromUser, record.toUser, record.projectId, record.fundValue, record.message, record.time);
    }
    
    function getRecordsByFromUser(uint256 _fromUser) public view returns(Record[] memory) {
        uint256 count = 0;
        uint256 i;
        for (i = 1; i < currentFundId; i++) {
            if (records[i].fromUser == _fromUser) {
                count++;
            }
        }
        Record[] memory result = new Record[](count);
        uint256 index = 0;
        for (i = 1; i < currentFundId; i++) {
            if (records[i].fromUser == _fromUser) {
                result[index] = records[i];
                index++;
            }
        }
        return result;
    }
    
    function getRecordsByToUser(uint256 _toUser) public view returns(Record[] memory) {
        uint256 count = 0;
        uint256 i;
        for (i = 1; i < currentFundId; i++) {
            if (records[i].toUser == _toUser) {
                count++;
            }
        }
        Record[] memory result = new Record[](count);
        uint256 index = 0;
        for (i = 1; i < currentFundId; i++) {
            if (records[i].toUser == _toUser) {
                result[index] = records[i];
                index++;
            }
        }
        return result;
    }
    
    function getRecordsByProjectId(uint256 _projectId) public view returns(Record[] memory) {
        uint256 count = 0;
        uint256 i;
        for (i = 1; i < currentFundId; i++) {
            if (records[i].projectId == _projectId) {
                count++;
            }
        }
        Record[] memory result = new Record[](count);
        uint256 index = 0;
        for (i = 1; i < currentFundId; i++) {
            if (records[i].projectId == _projectId) {
                result[index] = records[i];
                index++;
            }
        }
        return result;
    }
}
