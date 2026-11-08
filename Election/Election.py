import sys
from web3 import Web3
from solcx import compile_source, install_solc

w3 = Web3(Web3.HTTPProvider("http://127.0.0.1:8545"))
print("Connected to Ganache:", w3.is_connected())

install_solc("0.8.19")
compiled = compile_source(open("Voting.sol").read(), output_values=["abi", "bin"], solc_version="0.8.19")
contract = compiled["<stdin>:Voting"]

accounts = w3.eth.accounts
students = ["Alice", "Bruno", "Carla", "David", "Emma", "Felix", "Grace", "Hugo", "Iris", "Jack"]
tx = w3.eth.contract(abi=contract["abi"], bytecode=contract["bin"]).constructor().transact({"from": accounts[0]})
address = w3.eth.wait_for_transaction_receipt(tx).contractAddress
voting = w3.eth.contract(address=address, abi=contract["abi"])
print("Contract deployed at:", address)

if not (len(sys.argv) > 1 and sys.argv[1] == "test"):
    while True:
        print()
        print("========= VOTING MENU =========")
        print("1 - Show accounts")
        print("2 - Add a voter (owner only)")
        print("3 - Vote")
        print("4 - Show results")
        print("0 - Exit")
        option = input("Choose an option: ")

        try:
            if option == "1":
                for i in range(len(students)):
                    status = ""
                    if voting.functions.hasVoted(accounts[i]).call():
                        status = "already voted"
                    print(i, students[i], accounts[i], status)

            elif option == "2":
                number = int(input("Your student number (0-9): "))
                if voting.functions.hasVoted(accounts[number]).call():
                    raise Exception(students[number] + " already voted!")
                candidate = int(input("Choose a candidate (0 = Ken, 1 = Michael): "))
                if candidate != 0 and candidate != 1:
                    raise Exception(str(candidate) + " is not a candidate! Choose 0 = Ken or 1 = Michael.")
                tx = voting.functions.vote(candidate).transact({"from": accounts[number]})
                receipt = w3.eth.wait_for_transaction_receipt(tx)
                print(students[number] + ", your vote was registered on the blockchain!")
                print("Transaction:", w3.to_hex(tx))
                print("Block:", receipt.blockNumber, "| Gas used:", receipt.gasUsed)

            elif option == "3":
                print("Ken:", voting.functions.votes(0).call())
                print("Michael:", voting.functions.votes(1).call())

            elif option == "4":
                print("TODO: show results")
            elif option == "0":
                print("Goodbye!")
                break
            else:
                print("Invalid option, try again.")
        except Exception as e:
            print("Error:", e)
