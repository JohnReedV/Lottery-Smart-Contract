from brownie import accounts, network, config, Lottery


def deploy_lottery():
    account = get_account()
    lottery = Lottery.deploy({"from": account})


def get_account():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])


def main():
    deploy_lottery()
