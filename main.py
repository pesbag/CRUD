import logging
logger=logging.getLogger('shape')
logger.setLevel(logging.INFO)
formatter=logging.Formatter('%(asctime)s | %(levelname)s | %()s')
file_handler=logging.FileHandler('shape.log',encoding="utf-8")
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)

def main():
    pass
if __name__ == '__main__':
    main()