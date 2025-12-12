class Comment:
    # Клас, що представляє окремий коментар 
    
    def __init__(self, text, author):
    # Ініціалізує коментар з текстом, автором та порожнім списком відповідей.
        self.text = text
        self.author = author
        self.replies = []
        self.is_deleted = False

    def add_reply(self, reply_comment):
        # Додає відповідь до поточного коментаря.
        self.replies.append(reply_comment)

    def remove_reply(self):
        # Позначає коментар як видалений.
        self.text = "Цей коментар було видалено."
        self.author = ""
        self.is_deleted = True

    def display(self, indent=0):
        # Виводить коментар та всі його відповіді з відповідним відступом.
        prefix = " " * indent

        if self.is_deleted:
            print(f"{prefix}{self.text}")
        else:
            print(f"{prefix}{self.author}: {self.text}")

        for reply in self.replies:
            reply.display(indent + 4)



if __name__ == "__main__":
    root_comment = Comment("Яка чудова книга!", "Бодя")
    reply1 = Comment("Книга повне розчарування :(", "Андрій")
    reply2 = Comment("Що в ній чудового?", "Марина")

    root_comment.add_reply(reply1)
    root_comment.add_reply(reply2)

    reply1_1 = Comment(
        "Не книжка, а перевели купу паперу ні нащо...",
        "Сергій"
    )
    reply1.add_reply(reply1_1)

    reply1.remove_reply()

    root_comment.display()