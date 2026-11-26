# import torch

# data = torch.arange(1, 11)
# print(data[2:6])
# print(type(data))
# window_size = 4
# stride = 1

# windows = []

# a = len(data)
# print(a)

# for i in range(0, len(data) - window_size + 1, stride):
#     window = data[i:i + window_size]
#     windows.append(window)

# windows = torch.stack(windows)

# print(windows)

# import tiktoken

# enc = tiktoken.get_encoding("gpt2")
# text = "Hello, world. Is this a test!"

# integers = enc.encode(
#     text,
#     allowed_special={""}
# )
# print(integers)

# strings = enc.decode(integers)
# print(strings)

##################==================================
# from bpe_openai_gpt2 import get_encoder, download_vocab

# download_vocab()
# origin_text = get_encoder(model_name="gpt2_model", models_dir=".")
# integers = origin_text.encode("Hello, world!")
# print(integers)
# print(origin_text.decode(integers))
# ##################==================================

import transformers
transformers.