print("\n<<<<< 8-9 >>>>>")
def show_messages(messages):
    for msg in messages:
        print(msg)

messages = ["Hello","How is life?", "You can do it!"]
show_messages(messages)

print("\n<<<<< 8-10 >>>>>")
def send_message(messages, sent_messages):
    print("\nSending messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello","How is life?", "You can do it!"]
show_messages(messages)

sent_messages = []
send_message(messages, sent_messages)

print("\nFinal Lists:")
print(messages)
print(sent_messages)


print("\n<<<<< 8-11 >>>>>")
def send_message2(messages, sent_messages):
    print("\nSending messages:")
    while messages:
        current_message = messages.pop()
        print(current_message)
        sent_messages.append(current_message)

messages = ["Hello","How is life?", "You can do it!"]
show_messages(messages)

sent_messages = []
send_message2(messages[:], sent_messages)

print("\nFinal Lists:")
print(messages)
print(sent_messages)