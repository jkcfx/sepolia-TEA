🚀 使用教程：运行 daodaoshe_tea.py
🧰 一、安装 Python（建议 3.10+）
打开官网：https://www.python.org/downloads/

下载并安装，记得勾选 Add Python to PATH

安装后，打开命令行（终端）验证：

bash
复制
编辑
python --version
📦 二、安装依赖
在命令行中运行：

bash
复制
编辑
pip install web3
这是你程序唯一需要安装的第三方库，其它库都是 Python 内置的。

🔐 三、配置私钥（pks.txt）
在 daodaoshe_tea.py 文件所在目录，新建文件 pks.txt

用记事本或任意编辑器打开，在第一行粘贴你的以太坊私钥，例如：

复制
编辑
0x123abc...你的私钥
⚠️ 安全提示：请勿上传或分享此文件，推荐使用小额测试钱包。

▶️ 四、运行脚本
确保你在脚本所在目录，命令行中执行：

bash
复制
编辑
python daodaoshe_tea.py
✅ 示例目录结构如下：
复制
编辑
你的文件夹/
├── daodaoshe_tea.py
└── pks.txt
