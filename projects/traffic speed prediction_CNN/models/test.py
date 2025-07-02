


def test(net, partition, args):
    testloader = torch.utils.data.DataLoader(partition['test'],
                                             batch_size=args.test_batch_size,
                                             shuffle=False, num_workers=2)
    net.eval()

    mse_criterion = nn.MSELoss()    
    mae_criterion = nn.L1Loss()     

    test_mse = 0
    batch_orig_mse = 0 
    test_mae = 0
    test_mae_orig = 0  

    total = 0
    with torch.no_grad():
        for data in testloader:
            inputs, labels = data
            inputs = inputs.cuda()
            labels = labels.cuda()

            outputs = net(inputs)

            mse = mse_criterion(outputs, labels)
            mae = mae_criterion(outputs, labels)

            total += labels.size(0)
            test_mse += mse.item() * inputs.size(0)       
            test_mae += mae.item() * inputs.size(0)

            
            if y_scaler is not None:
                outputs_np = outputs.detach().cpu().numpy().reshape(-1, 2)
                labels_np = labels.detach().cpu().numpy().reshape(-1, 2)

                outputs_orig = y_scaler.inverse_transform(outputs_np).reshape(outputs.shape)
                labels_orig = y_scaler.inverse_transform(labels_np).reshape(labels.shape)

                batch_mae = np.mean(np.abs(outputs_orig - labels_orig))
                test_mae_orig += batch_mae * inputs.size(0)
                orig_loss = np.mean((outputs_orig - labels_orig)**2)
                batch_orig_mse += orig_loss.item() * inputs.size(0)

        test_mse_loss = test_mse / total
        test_orig_loss = batch_orig_mse / total if y_scaler is not None else None
        test_mae_loss = test_mae / total
        test_mae_orig_loss = test_mae_orig / total if y_scaler is not None else None

    return test_mse_loss, test_orig_loss, test_mae_loss, test_mae_orig_loss

