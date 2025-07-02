def train(net, partition, optimizer, criterion, args):
    trainloader = torch.utils.data.DataLoader(partition['train'],
                                              batch_size=args.train_batch_size,
                                              shuffle=True, num_workers=2)
    net.train()
    mae_criterion = nn.L1Loss()  

    total = 0
    train_loss = 0.0
    train_mae = 0     
    batch_orig_mse = 0 
    for i, data in enumerate(trainloader, 0):
        optimizer.zero_grad() 
      
        inputs, labels = data
        inputs = inputs.cuda()
        labels = labels.cuda()
        outputs = net(inputs)

        loss = criterion(outputs, labels)
        loss.backward()
        optimizer.step()

        train_loss += loss.item() * inputs.size(0)    
        total += labels.size(0)
        mae = mae_criterion(outputs, labels)
        train_mae += mae.item() * inputs.size(0)   

        
        if y_scaler is not None:
            outputs_np = outputs.detach().cpu().numpy().reshape(-1, 2)
            labels_np = labels.detach().cpu().numpy().reshape(-1, 2)

            outputs_orig = y_scaler.inverse_transform(outputs_np).reshape(outputs.shape)
            labels_orig = y_scaler.inverse_transform(labels_np).reshape(labels.shape)

            orig_loss = np.mean((outputs_orig - labels_orig)**2)
            batch_orig_mse += orig_loss.item() * inputs.size(0)

    train_loss = train_loss / total
    train_mae_loss = train_mae / total  
    train_orig_loss = batch_orig_mse / total if y_scaler is not None else None

    return net, train_loss, train_orig_loss, train_mae_loss    
