| **接口名**                    | **描述**                               | **参数**                                                           |
| ----------------------------------- | -------------------------------------------- | ------------------------------------------------------------------------ |
| getNodeVersion                      | 获取区块链节点版本信息                       | 无                                                                       |
| getBlockNumber                      | 获取最新块高                                 | 无                                                                       |
| getPbftView                         | 获取PBFT视图                                 | 无                                                                       |
| getSealerList                       | 获取共识节点列表                             | 无                                                                       |
| getObserverList                     | 获取观察者节点列表                           | 无                                                                       |
| getConsensusStatus                  | 获取区块链节点共识状态                       | 无                                                                       |
| getSyncStatus                       | 获取区块链节点同步状态                       | 无                                                                       |
| getPeers                            | 获取区块链节点的连接信息                     | 无                                                                       |
| getGroupPeers                       | 获取指定群组的共识节点``和观察节点列表       | 无                                                                       |
| getNodeIDList                       | 获取节点及其连接节点的列表                   | 无                                                                       |
| getGroupList                        | 获取节点所属群组的群组ID列表                 | 无                                                                       |
| getBlockByHash                      | 根据区块哈希获取区块信息                     | 区块哈希                                                                 |
| getBlockByNumber                    | 根据区块高度获取区块信息                     | 区块高度                                                                 |
| getBlockHashByNumber                | 根据区块高度获取区块哈希                     | 区块高度                                                                 |
| getTransactionByHash                | 根据交易哈希获取交易信息                     | 交易哈希                                                                 |
| getTransactionByBlockHashAndIndex   | 根据交易所属的区块哈希、交易索引获取交易信息 | 交易所属的区块哈希、交易索引                                             |
| getTransactionByBlockNumberAndIndex | 根据交易所属的区块高度、交易索引获取交易信息 | 交易所属的区块高度、交易索引                                             |
| getTransactionReceipt               | 根据交易哈希获取交易回执                     | 交易哈希                                                                 |
| getPendingTransactions              | 获取交易池内所有未上链的交易                 | 无                                                                       |
| getPendingTxSize                    | 获取交易池内未上链的交易数目                 | 无                                                                       |
| getCode                             | 根据合约地址查询的合约数据                   | 合约地址                                                                 |
| getTotalTransactionCount            | 获取指定群组的上链交易数目                   | 无                                                                       |
| getSystemConfigByKey                | 获取系统配置                                 | 系统配置关键字，如：<br />- tx_count_limit<br />- tx_gas_limit           |
| deploy                              | 部署合约                                     | 合约binary code                                                          |
| call                                | 调用合约                                     | 合约地址 <br />合约abi<br /> 调用接口名称 <br />参数列表                 |
| sendRawTransaction                  | 发送交易                                     | 合约地址 <br />合约abi <br />接口名 <br />参数列表 <br />合约binary code |
| sendRawTransactionGetReceipt        | 发送交易并获取交易执行结果                   | 合约地址 <br />合约abi接口名 <br />参数列表 <br />合约binary code        |
