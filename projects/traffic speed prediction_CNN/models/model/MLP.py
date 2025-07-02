class MLP(nn.Module):
    def __init__(self, in_shape, out_dim, hid_dim, n_layer, act, dropout, use_bn):
        super(MLP, self).__init__()

        # ====== Create Activation Function ====== #
        if act == 'relu':            
            self.act = nn.ReLU()
        elif act == 'tanh':
            self.act = nn.Tanh()
        elif act == 'sigmoid':
            self.act = nn.Sigmoid()
        else:
            raise ValueError('No valid activation function selected!')

        self.in_dim = in_shape[1]*in_shape[2]*in_shape[3]
        self.out_dim = out_dim
        self.hid_dim = hid_dim
        self.n_layer = n_layer
        self.act_name = act      
        self.dropout = dropout
        self.use_bn = use_bn


        # ===== Create layers ====== #
        layers = [
            nn.Linear(self.in_dim, hid_dim),
            self.act,
                ]
        if use_bn:
            layers.append(nn.BatchNorm1d(hid_dim))

        layers.append(nn.Dropout(dropout))

        for _ in range(n_layer - 1):
            layers.append(nn.Linear(hid_dim, hid_dim))
            layers.append(self.act)
            if use_bn:
                layers.append(nn.BatchNorm1d(hid_dim))

            layers.append(nn.Dropout(dropout))

        layers.append(nn.Linear(hid_dim, out_dim))

        self.classifier = nn.Sequential(*layers)


        # ====== Create Regularization Layer ======= #
        self.dropout = nn.Dropout(self.dropout)
        #if self.use_xavier:
        #    self.xavier_init()

    def forward(self, x):
        x= x.view(x.size(0),-1) 
        x = self.classifier(x)
        x = x.view(x.size(0), 1, 304, 2)
        return x
