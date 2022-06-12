

--create database major -- execute if major database does not exist



create table [major].[dbo].tb_ships(
 ship_id int primary key identity(1,1),
 ship_capacity int
 --ship_unload_Quantity int,
 --ship_load_Quantity int,
)


create table [major].[dbo].tb_container(
 container_id int primary key identity(1,1),
 ship_id int foreign key references [major].[dbo].tb_ships (ship_id),
 container_desination varchar(10),
 container_origin varchar(10),
 container_start_date date,
 container_delivery_date date,
 container_shape int,
 container_priority bit,
)



create table [major].[dbo].tb_container_spaces(
space_id int primary key identity(1,1),
sub_space_count int
)

create table [major].[dbo].tb_subspace(
subspace_id int primary key identity(1,1),
space_id int foreign key references [major].[dbo].tb_container_spaces (space_id),
max_stack_capacity int,
current_capacity int
)

create table [major].[dbo].tb_subspace_stack(

stack_id int primary key identity(1,1),
space_id int foreign key references [major].[dbo].tb_container_spaces (space_id),
subspace_id int foreign key references [major].[dbo].tb_subspace (subspace_id),
container_id int foreign key references [major].[dbo].tb_container (container_id),
container_final_destination_reached bit, --1 reached 0 not reached
container_slot_status bit, --1 container 0 no container 
container_reached_date date,

)



