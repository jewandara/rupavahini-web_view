
DROP TABLE IF EXISTS `alarm_ca_alarms_tb`;
CREATE TABLE IF NOT EXISTS `alarm_ca_alarms_tb` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `did` int(12) NOT NULL,
  `cid` int(12) NOT NULL,
  `alarmstate` varchar(20) DEFAULT NULL,
  `mhandle` varchar(20) DEFAULT NULL,
  `mthandle` varchar(20) DEFAULT NULL,
  `ackd` varchar(10) DEFAULT NULL,
  `clearable` varchar(10) DEFAULT NULL,
  `ca_down_uniq` int(12) DEFAULT NULL,
  `ca_down_specific` int(2) DEFAULT NULL,
  `ca_down_time` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `sql_down_update` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  `ca_down_comment` varchar(100) DEFAULT NULL,
  `ca_up_uniq` int(12) DEFAULT NULL,
  `ca_up_specific` int(2) DEFAULT NULL,
  `ca_up_time` datetime DEFAULT NULL,
  `sql_up_update` datetime DEFAULT NULL,
  `ca_up_comment` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
);



DROP TABLE IF EXISTS `alarm_ca_alarm_category_tb`;
CREATE TABLE IF NOT EXISTS `alarm_ca_alarm_category_tb` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(500) NOT NULL,
  `status` varchar(10) NOT NULL,
  `minutes_threshold_value` int(11) NOT NULL DEFAULT '43200',
  `ignore_minutes_threshold` bit(1) NOT NULL DEFAULT b'0',
  `ignore_specific_threshold` bit(1) NOT NULL DEFAULT b'1',
  `description` text,
  `example` varchar(2000) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `category` (`category`)
);




DROP TABLE IF EXISTS `alarm_ca_devices_tb`;
CREATE TABLE IF NOT EXISTS `alarm_ca_devices_tb` (
  `id` int(12) NOT NULL AUTO_INCREMENT,
  `ip` varchar(20) DEFAULT NULL,
  `type` varchar(200) DEFAULT NULL,
  `name` varchar(2000) DEFAULT NULL,
  `date` datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`),
  UNIQUE KEY `ip` (`ip`)
);



DROP TABLE IF EXISTS `alarm_ca_solution_tb`;
CREATE TABLE IF NOT EXISTS `alarm_ca_solution_tb` (
  `did` int(12) NOT NULL,
  `num` int(12) NOT NULL
);

