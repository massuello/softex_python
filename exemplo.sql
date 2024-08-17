INSERT INTO Cliente (id_cliente, nome, email, endereco) VALUES 
(1, 'Maria Silva', 'maria.silva@example.com', 'Rua das Flores, 123'),
(2, 'João Pereira', 'joao.pereira@example.com', 'Av. Brasil, 456'),
(3, 'Ana Costa', 'ana.costa@example.com', 'Rua da Paz, 789'),
(4, 'Carlos Santos', 'carlos.santos@example.com', 'Rua Verde, 101'),
(5, 'Juliana Lima', 'juliana.lima@example.com', 'Av. Mar, 202');

INSERT INTO Produto (id_produto, nome, preco, categoria) VALUES 
(1, 'Notebook', 3500.00, 'Eletrônicos'),
(2, 'Smartphone', 2000.00, 'Eletrônicos'),
(3, 'Geladeira', 1800.00, 'Eletrodomésticos'),
(4, 'Cafeteira', 150.00, 'Eletrodomésticos'),
(5, 'Bicicleta', 800.00, 'Esportes');

INSERT INTO Pedido (id_pedido, data_pedido, id_cliente) VALUES 
(1, '2024-07-25 10:30:00', 1),
(2, '2024-07-26 14:45:00', 2),
(3, '2024-07-27 09:15:00', 3),
(4, '2024-07-28 11:00:00', 4),
(5, '2024-07-29 16:30:00', 5);

INSERT INTO ItemPedido (id_itemPedido, quantidade, id_pedido, id_produto) VALUES 
(1, 1, 1, 1),
(2, 2, 1, 4),
(3, 1, 2, 2),
(4, 1, 2, 5),
(5, 1, 3, 3),
(6, 2, 4, 1),
(7, 1, 4, 4),
(8, 3, 5, 5),
(9, 1, 5, 2),
(10, 2, 3, 4);
