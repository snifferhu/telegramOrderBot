CREATE TABLE `deposit_list` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`tele_id` VARCHAR(50) NULL DEFAULT NULL,
	`price` DECIMAL(10,3) NULL DEFAULT NULL,
	`bef` DECIMAL(10,3) NULL DEFAULT NULL,
	`aft` DECIMAL(10,3) NULL DEFAULT NULL,
	`create_time` TIMESTAMP NOT NULL DEFAULT '',
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=945
;

CREATE TABLE `driver_list` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`tele_id` VARCHAR(50) NOT NULL DEFAULT '0',
	`store_id` VARCHAR(50) NOT NULL DEFAULT '0',
	`create_time` TIMESTAMP NOT NULL DEFAULT '',
	`update_time` TIMESTAMP NOT NULL DEFAULT '',
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `follow_list` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`driver_id` VARCHAR(50) NOT NULL DEFAULT '0',
	`follow_id` VARCHAR(50) NOT NULL DEFAULT '0',
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `member` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`name` VARCHAR(50) NULL DEFAULT '0',
	`nickName` VARCHAR(50) NULL DEFAULT '0',
	`amout` DECIMAL(10,3) NOT NULL DEFAULT '0',
	`create_time` TIMESTAMP NOT NULL DEFAULT '',
	`update_time` TIMESTAMP NOT NULL DEFAULT '',
	`tele_id` VARCHAR(50) NULL,
	`phone` VARCHAR(50) NULL,
	`is_driver` INT(11) NULL DEFAULT '0',
	`driver_id` VARCHAR(50) NULL DEFAULT '1',
	PRIMARY KEY (`id`),
	UNIQUE INDEX `name` (`name`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
AUTO_INCREMENT=96
;

CREATE TABLE `order_info` (
	`id` VARCHAR(50) NOT NULL,
	`member_id` VARCHAR(50) NOT NULL DEFAULT '0',
	`nick_name` VARCHAR(50) NOT NULL DEFAULT '0',
	`price` DECIMAL(10,3) NOT NULL DEFAULT '0',
	`item` VARCHAR(50) NOT NULL DEFAULT '0',
	`order_status` VARCHAR(50) NOT NULL DEFAULT '0',
	`create_time` TIMESTAMP NOT NULL DEFAULT '',
	`update_time` TIMESTAMP NOT NULL DEFAULT '',
	`driver_id` VARCHAR(50) NULL DEFAULT '1',
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

CREATE TABLE `store_info` (
	`id` INT(11) NOT NULL AUTO_INCREMENT,
	`store_title` VARCHAR(50) NOT NULL DEFAULT '0',
	`store_id` VARCHAR(50) NOT NULL DEFAULT '0',
	`menu_title` VARCHAR(50) NOT NULL DEFAULT '0',
	`info` VARCHAR(500) NOT NULL DEFAULT '0',
	`create_time` TIMESTAMP NOT NULL DEFAULT '',
	`update_time` TIMESTAMP NOT NULL DEFAULT '',
	PRIMARY KEY (`id`)
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;

CREATE TABLE fate.balance_info
(
    id INT PRIMARY KEY,
    tele_id VARCHAR(50),
    nick_name VARCHAR(50),
    amount DECIMAL(9,3),
    driver_id INT,
    driver_tele_id VARCHAR(50),
    create_time timestamp default CURRENT_TIMESTAMP not null,
	  update_time timestamp default CURRENT_TIMESTAMP not null
)
COLLATE='utf8_general_ci'
ENGINE=InnoDB
;