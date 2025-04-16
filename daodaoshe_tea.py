from web3 import Web3
import random
import os
import time
from datetime import datetime, timedelta, timezone

# 指定 EVM 链（以 Ethereum 为例）
RPC_URL = "https://tea-sepolia.g.alchemy.com/public"
web3 = Web3(Web3.HTTPProvider(RPC_URL))

# 发送者账户信息
# 读取私钥列表
def load_private_keys(file_path="pks.txt"):
    try:
        with open(file_path, "r") as f:
            keys = [line.strip() for line in f if line.strip()]
        print(f"成功加载 {len(keys)} 个私钥")
        return keys
    except Exception as e:
        print(f"加载私钥文件失败: {e}")
        return []

private_keys = load_private_keys()
private_key = private_keys[0] if private_keys else None
from_account = web3.eth.account.from_key(private_key).address
def get_random_recipient():
    try:
        try:
            latest_block = web3.eth.get_block("latest", full_transactions=False)
            tx_hash_list = latest_block.transactions
        except Exception as e:
            print(f"获取区块失败: {e}")
            return web3.to_checksum_address("0x" + os.urandom(20).hex())

        valid_recipients = []

        for tx_hash in tx_hash_list:
            try:
                tx = web3.eth.get_transaction(tx_hash)
                to_addr = tx.get("to")
                if to_addr and web3.is_address(to_addr):
                    to_addr = web3.to_checksum_address(to_addr)
                    code = web3.eth.get_code(to_addr)
                    if not code or code == b"" or code == b"0x":
                        return to_addr
            except Exception as inner_e:
                print(f"处理交易 {tx_hash.hex()} 失败: {inner_e}")

        if valid_recipients:
            recipient = random.choice(valid_recipients)
        else:
            print("区块中未找到有效地址，生成随机地址作为接收方")
            recipient = web3.to_checksum_address("0x" + os.urandom(20).hex())

        return recipient
    except Exception as e:
        print(f"获取随机地址失败: {e}，使用备用随机地址")
        return web3.to_checksum_address("0x" + os.urandom(20).hex())


def send_transaction(recipient):
    try:
        amount = web3.to_wei(round(random.uniform(0.001, 0.006), 3), "ether")
        nonce = web3.eth.get_transaction_count(from_account, 'pending')
        print(f"nonce: {nonce}")
        gasPrice = web3.eth.gas_price * 2
        gasGwei = Web3.from_wei(gasPrice, "gwei")
        print(f"gasPriceGwei: {gasGwei}")
        tx_data = {
            "nonce": nonce,
            "to": recipient,
            "value": amount,
            "gasPrice": gasPrice,
        }
        #time.sleep(random.randint(21, 75))
        try:
            gas = 21000
            tx_data["gas"] = gas
            print(f"✅ 估算 Gas 成功: {gas}")
        except Exception as e:
            fallback_gas = 21000  # 最小转账交易 gas，适用于普通转账
            tx_data["gas"] = fallback_gas
            print(f"⚠️ 估算 Gas 失败: {e}，使用备用 gas: {fallback_gas}")

        
        signed_tx = web3.eth.account.sign_transaction(tx_data, private_key)
        tx_hash = web3.eth.send_raw_transaction(signed_tx.rawTransaction)
        
        print(f"[{web3.eth.block_number}] 发送 {amount / 1e18:.4f} ETH 到 {recipient}，交易哈希: {tx_hash.hex()}")
    except Exception as e:
        print(f"交易失败: {e}")
# 循环 10 次

while True:
    # now = datetime.now(timezone.utc) + timedelta(hours=8)
    
    # start_hour = random.randint(8, 9)
    # start_minute = random.randint(0, 59)
    # start_time = now.replace(hour=start_hour, minute=start_minute, second=0, microsecond=0)
    
    # if start_time < now:
        # start_time += timedelta(days=1)
    
    # time_to_wait = (start_time - now).total_seconds()
    # print(f"将在 {start_time} (UTC+8) 开始执行...")
    # time.sleep(time_to_wait)

    # 依次使用随机私钥进行交易
    num = random.randint(110, 125)
    recipient = get_random_recipient()
    for i in range(num):
        if i == 0:
            send_transaction(web3.to_checksum_address("0xD8c4bcA831FDa39e310EF8580Ec092492D8B66CB"))  # 第一次循环执行方法 a
            time.sleep(random.randint(21, 55))
        else:
            send_transaction(recipient)
            time.sleep(random.randint(21, 55))
    print("今日任务完成，等待明天...")
    
    # 计算到明天 9:00 之间的等待时间
    now = datetime.now(timezone.utc) + timedelta(hours=8)
    next_day = now + timedelta(days=1)
    next_start_time = next_day.replace(hour=8, minute=0, second=0, microsecond=0)
    sleep_time = (next_start_time - now).total_seconds()
    print(f"休眠至 {next_start_time} (UTC+8)...")
    time.sleep(sleep_time)