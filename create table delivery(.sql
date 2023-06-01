create table delivery(
	delivery_id serial primary key,
	address_id int references address(address_id) not null,
	delivery_date date not null,
	time_range text[] not null,
	staff_id int references staff(staff_id) not null,
	status del_status not null default 'в обработке',
	last_update timestamp,
	create_date timestamp default now(),
	deleted boolean not null default false
)


alter table orders add constraint orders_delivery_fkey foreign key (delivery_id)
	references delivery(delivery_id)
	
insert into delivery (address_id, delivery_date, time_range, staff_id)
values(102, '2022.2.25', array['10:00:00', '18:00:00'], 2),
(34, '2022.2.25', array['10:00:00', '18:00:00'], 2),
(12, '2022.2.25', array['10:00:00', '18:00:00'], 2),
(2, '2022.2.25', array['10:00:00', '18:00:00'], 2),
(99, '2022.2.25', array['10:00:00', '18:00:00'], 2)

update orders
set delivery_id = 1
where order_id = 1

update orders
set delivery_id = 2
where order_id = 2

update orders
set delivery_id = 3
where order_id = 3

update orders
set delivery_id = 4
where order_id = 4

update orders
set delivery_id = 5
where order_id = 5

select * from orders 

select * from delivery

delete from delivery 
where delivery_id = 1
