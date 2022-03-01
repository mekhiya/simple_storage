from brownie import SimpleStorage, accounts


def test_deploy():
    # Arrange
    account = accounts[0]
    # Act
    simple_storage = SimpleStorage.deploy({"from": account})
    starting_value = simple_storage.retrieve()
    expected = 0
    # Assert
    assert starting_value == 0


def test_updating_value():
    # Arrange
    account = accounts[0]
    simple_storage = SimpleStorage.deploy({"from": account})
    expected_value = 15
    tx = simple_storage.store(expected_value, {"from": account})
    tx.wait(1)
    # Act
    assert expected_value == simple_storage.retrieve()

    # Assert
