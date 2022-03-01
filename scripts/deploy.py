from brownie import accounts, config, SimpleStorage, network


def deploy_simple_storage():
    account = get_accounts()
    # account = accounts[0]  # works with local ganache account
    # account = accounts.add(config["wallets"]["from_key"])
    print(account)
    simple_storage = SimpleStorage.deploy({"from": account})
    print(simple_storage)
    stored_value = simple_storage.retrieve()
    print(stored_value)
    tx = simple_storage.store(15, {"from": account})
    tx.wait(1)
    new_value = simple_storage.retrieve()
    print(new_value)


def main():
    deploy_simple_storage()


def get_accounts():
    if network.show_active() == "development":
        return accounts[0]
    else:
        return accounts.add(config["wallets"]["from_key"])
