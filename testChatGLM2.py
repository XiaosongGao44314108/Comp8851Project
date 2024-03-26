from transformers import AutoTokenizer, AutoModel

def main():
    tokenizer = AutoTokenizer.from_pretrained("THUDM/chatglm2-6b-int4", trust_remote_code=True)
    model = AutoModel.from_pretrained("THUDM/chatglm2-6b-int4", trust_remote_code=True).half().cuda()
    model = model.eval()
    response, history = model.chat(tokenizer, "hello", history=[])
    print(response)

    response, history = model.chat(tokenizer, "can u print a hello world message by python？", history=history)
    print(response)
    
if __name__ == '__main__':
    main()
