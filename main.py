"""
This is a file test add-on for DocumentCloud.
"""

from documentcloud.addon import AddOn


class FileTest(AddOn):

    def main(self):
        content = self.get_file("file")
        print(content)
        size = len(content)
        self.set_message(f"File size: {size}")


if __name__ == "__main__":
    FileTest().main()
