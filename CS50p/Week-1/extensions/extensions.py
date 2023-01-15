
IMAGE_FILE_EXTENSIONS = ["jpg", "jpeg", "png", "gif"]
APP_FILE_EXTENSIONS = ["pdf", "zip"]
TEXT_FILE_EXTENSIONS = "txt"
DEFAULT_FILE_EXTENSIONS = "octet-stream"

def main():
    user_input = input("Filename: ")
    user_input = user_input.strip()
    user_input = user_input.lower()

    if user_input.endswith(tuple(IMAGE_FILE_EXTENSIONS)):
        for extension in IMAGE_FILE_EXTENSIONS:
            if user_input.endswith(extension):
                if extension == "jpg":
                    print("image/jpeg")
                else:
                    print("image/" + extension)

    elif user_input.endswith(tuple(APP_FILE_EXTENSIONS)):
        for extension in APP_FILE_EXTENSIONS:
            if user_input.endswith(extension):
                print("application/" + extension)

    elif user_input.endswith(TEXT_FILE_EXTENSIONS):
        print("text/plain")

    else:
        print("application/" + DEFAULT_FILE_EXTENSIONS)


if __name__ == "__main__":
    main()