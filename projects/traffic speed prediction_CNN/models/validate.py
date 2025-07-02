def validate(net, partition, criterion, args):
    valloader = torch.utils.data.DataLoader(partition['val'],
                                            batch_size=args.test_batch_size,
                                            shuffle=False, num_workers=2)
    net.eval()

    mae_criterion = nn.L1Loss()   

    total = 0
    val_loss = 0
    batch_orig_mse = 0 
    val_mae = 0       
    val_mae_orig = 0  

    with torch.no_grad():
        for data in valloader:
            inputs, labels = data
            inputs = inputs.cuda()
            labels = labels.cuda()
            outputs = net(inputs)

            loss = criterion(outputs, labels)
            val_loss += loss.item() * inputs.size(0)
            total += labels.size(0)

            mae = mae_criterion(outputs, labels)
            val_mae += mae.item() * inputs.size(0)     

            if y_scaler is not None:
                outputs_np = outputs.detach().cpu().numpy().reshape(-1, 2)
                labels_np = labels.detach().cpu().numpy().reshape(-1, 2)

                outputs_orig = y_scaler.inverse_transform(outputs_np).reshape(outputs.shape)
                labels_orig = y_scaler.inverse_transform(labels_np).reshape(labels.shape)

                batch_mae = np.mean(np.abs(outputs_orig - labels_orig))
                val_mae_orig += batch_mae * inputs.size(0)
                orig_loss = np.mean((outputs_orig - labels_orig)**2)
                batch_orig_mse += orig_loss.item() * inputs.size(0)

        val_loss = val_loss / total
        val_orig_loss = batch_orig_mse / total if y_scaler is not None else None
        val_mae_loss = val_mae / total
        val_mae_orig_loss = val_mae_orig / total if y_scaler is not None else None

    return val_loss, val_orig_loss, val_mae_loss, val_mae_orig_loss
