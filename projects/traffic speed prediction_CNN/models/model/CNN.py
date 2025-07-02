class CNN(nn.Module):

    def __init__(self, model_code, in_channels, out_dim, act, use_bn, dropout, hid_dim):
        super(CNN, self).__init__()

        if act == 'relu' :
            self.act = nn.ReLU()
        elif act == 'sigmoid' :
            self.act = nn.Sigmoid()
        elif act == 'tanh' :
            self.act = nn.Tanh()
        else :
            raise ValueError("Not a valid activation function code")

        self.layers = self._make_layers(model_code, in_channels, use_bn)  
        dummy_input = torch.zeros(1, in_channels, 304, 8)   
        flatten_size = self._get_flattened_size(dummy_input)  
        self.classifier = nn.Sequential(nn.Linear(flatten_size, out_dim))


    def forward(self, x):         
        x = self.layers(x)
        #print("Before flatten:", x.shape)

        x = x.view(x.size(0), -1)
        #print("After flatten:", x.shape)

        x = self.classifier(x)
        x = x.view(x.size(0), 1, 304, 2)   
        return x

    def _make_layers(self, model_code, in_channels, use_bn) :   
        layers = []

        if cfg[model_code] == []:
            self.is_mlp_mode = True     
            return nn.Identity()

        else:
          self.is_mlp_mode = False
          for x in cfg[model_code] :
              if x == 'M':
                  layers += [nn.MaxPool2d(kernel_size =2, stride = 2)]

              else:
                  layers += [nn.Conv2d(in_channels=in_channels,
                                      out_channels = x,
                                      kernel_size=3,
                                      stride =1,
                                      padding =1) ]

                  if use_bn :
                        layers += [nn.BatchNorm2d(x)]           
                  layers += [self.act]

                  in_channels = x
          return nn.Sequential(*layers)      

    
    def _get_flattened_size(self, x) :        
        x = self.layers(x)
        return x.view(x.size(0), -1).size(1)
