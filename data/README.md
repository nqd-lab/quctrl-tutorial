This directory contains the data files. 

We distinguish between generative models, raw data, and processed data. For instance, a Monte-Carlo simulation of the Ising model can generate samples which constitute the raw data; by contrast, the magnetization computed from these samples is an example of processed data. Trained neural networks (or other quantities undergoing optimization such as MPS/MPO), on the other hand, correspond to generative models (i.e., models which generate data). Note that hyperparameters should go in `src_code/config/` instead. 

If the raw data is >50 GB but <200 GB, we can request more storage. In such cases, we should discuss what the best way to proceed is. 

_Try to stick to single data format if possible; don't make a soup out of your favorite file types. Whenever possible, use data formats which are universal (i.e., do not require any proprietary software to read and can be opened with the default tools in a unix terminal)._