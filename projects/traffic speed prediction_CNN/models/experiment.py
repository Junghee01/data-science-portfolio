def experiment(partition, args):
    trainloader = torch.utils.data.DataLoader(
        partition['train'],
        batch_size=args.train_batch_size,
        shuffle=True,
        num_workers=2
          )

    sample_inputs, _ = next(iter(trainloader))  
    sample_inputs = sample_inputs.cuda()
    in_shape = sample_inputs.shape               

    if args.model_type == 'CNN':
        net = CNN(model_code = args.model_code,
                  in_channels = args.in_channels,
                  out_dim = args.out_dim,
                  act = args.act,
                  use_bn= args.use_bn,
                  dropout = args.dropout,
                  hid_dim = args.hid_dim)

    elif args.model_type == 'MLP':
        net = MLP(
            in_shape=in_shape,
            out_dim=args.out_dim,
            hid_dim=args.hid_dim,
            n_layer=args.n_layer,
            act=args.act,
            dropout=args.dropout,
            use_bn=args.use_bn
        )
    else:
        raise ValueError(f"Invalid model_type: {args.model_type}")

    net.cuda()

    criterion = nn.MSELoss()  
    if args.optim == 'SGD':
        optimizer = optim.RMSprop(net.parameters(), lr=args.lr, weight_decay=args.l2)  # L2 reularization optizimer 의 weight_decay 에서 설정함!
    elif args.optim == 'RMSprop':
        optimizer = optim.RMSprop(net.parameters(), lr=args.lr, weight_decay=args.l2)
    elif args.optim == 'Adam':
        optimizer = optim.Adam(net.parameters(), lr=args.lr, weight_decay=args.l2)
    else:
        raise ValueError('In-valid optimizer choice')


    early_stopping = EarlyStopping(patience=7, min_delta=0.00001) if args.use_early_stopping else None



    scheduler = optim.lr_scheduler.ReduceLROnPlateau(
        optimizer, mode='min', patience=3, factor=0.1, min_lr=1e-6,
        threshold=1e-3, threshold_mode='abs') if args.use_scheduler else None                  
    # ===== List for epoch-wise data ====== #
    train_losses = []
    val_losses = []
    train_mae_losses = []
    val_mae_losses = []
    val_mae_orig_losses = []
    # ===================================== #
    best_metric = float('inf')

    for epoch in range(args.epoch):  
        ts = time.time()
        net, train_loss, train_orig_loss, train_mae_loss = train(net, partition, optimizer, criterion, args)
        val_loss, val_orig_loss, val_mae_loss, val_mae_orig_loss = validate(net, partition, criterion, args)
        te = time.time()

        if args.use_scheduler:
            scheduler.step(val_loss)

        if args.use_early_stopping:
            early_stopping(val_loss)
            if early_stopping.early_stop :
                  print("Early stopping triggered!")
                  break


        # ====== Add Epoch Data ====== #
        train_losses.append(train_loss)
        val_losses.append(val_loss)
        train_mae_losses.append(train_mae_loss)
        val_mae_losses.append(val_mae_loss)
        val_mae_orig_losses.append(val_mae_orig_loss)
        # ============================ #

        setting = deepcopy(vars(args))
        del setting['epoch']
        hash_key = hashlib.sha1(str(setting).encode()).hexdigest()[:6]
        os.makedirs('./checkpoints', exist_ok=True)                     
        model_path = f'./checkpoints/{args.exp_name}-{hash_key}.pth'    

        if val_loss < best_metric:
            best_metric = val_loss
            torch.save(net.state_dict(), model_path)                   

        current_lr = scheduler.get_last_lr()[0] if args.use_scheduler else args.lr
        print('Epoch {}, Loss(train/val) {:2.4f}/{:2.4f}, MAELoss(train/val) {:2.4f}/{:2.4f}, MAE_origLoss(val) {:2.4f}. Took {:2.2f} sec, Current LR {:2.6f}'.format(epoch, train_loss, val_loss, train_mae_loss, val_mae_loss, val_mae_orig_loss, te-ts, current_lr))

    test_loss, test_orig_loss, test_mae_loss, test_mae_orig_loss = test(net, partition, args)

    # ======= Add Result to Dictionary ======= #
    result = {}
    result['train_losses'] = train_losses
    result['val_losses'] = val_losses
    result['train_mae_losses'] = train_mae_losses
    result['val_mae_losses'] = val_mae_losses
    result['val_mae_orig_losses'] = val_mae_orig_losses
    result['train_mse'] = train_loss   
    result['val_mse'] = val_loss       
    result['test_mse'] = test_loss   
    result['train_mae'] = train_mae_loss   
    result['val_mae'] = val_mae_loss      
    result['test_mae'] = test_mae_loss     
    result['train_orig_loss'] = train_orig_loss
    result['test_orig_loss'] = test_orig_loss        
    result['val_mae_orig_loss'] = val_mae_orig_loss  
    result['test_mae_orig_loss'] = test_mae_orig_loss 

    return vars(args), result        
    # ===================================== #
