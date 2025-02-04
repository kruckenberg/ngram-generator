from model import NgramLM

def main():
    # set n-gram size
    n = 4

    # choose texts to include in training
    dev = False
    gatsby = True
    pride_prejudice = True
    sherlock = True

    # build corpus list
    training_corpus = []
    if dev:
        training_corpus.append('./train/dev.txt')
    if gatsby:
        training_corpus.append('./train/great_gatsby.txt')
    if pride_prejudice:
        training_corpus.append('./train/pride_and_prejudice.txt')
    if sherlock:
        training_corpus.append('./train/sherlock_holmes.txt')


    model = NgramLM(n)
    for path in training_corpus:
        with open(path, 'r') as f:
            text = f.read()
        print(f'Training on {path}')
        model.train(text)

    generate_text = True
    length = 20
    while generate_text:
        seed = input('prompt: ')
        if not seed:
            generate_text = False
            break
        print(model.generate(length, seed))

if __name__ == '__main__':
    main()