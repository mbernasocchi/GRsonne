﻿--
-- SQL dump automatically generated by "spatialite_gui" [GPLv3]
-- created on: 2014-06-25 15:56:48
--
-- DB-file origin: /home/marco/Documents/work/QGIS/renewables-now.com/gr_sonne/test.sqlite
-- Table origin: "test"
--
-- intended target is: PostgreSQL + PostGIS
--

CREATE SCHEMA IF NOT EXISTS "gr_sonne";

CREATE TABLE "gr_sonne"."irradiation" (
	"id" integer PRIMARY KEY,
	"x" integer,
	"y" integer,
	"ixxx_00" integer,
	"i000_10" integer,
	"i000_20" integer,
	"i000_30" integer,
	"i000_40" integer,
	"i000_50" integer,
	"i000_60" integer,
	"i000_70" integer,
	"i000_80" integer,
	"i000_90" integer,
	"i020_10" integer,
	"i020_20" integer,
	"i020_30" integer,
	"i020_40" integer,
	"i020_50" integer,
	"i020_60" integer,
	"i020_70" integer,
	"i020_80" integer,
	"i020_90" integer,
	"i040_10" integer,
	"i040_20" integer,
	"i040_30" integer,
	"i040_40" integer,
	"i040_50" integer,
	"i040_60" integer,
	"i040_70" integer,
	"i040_80" integer,
	"i040_90" integer,
	"i060_10" integer,
	"i060_20" integer,
	"i060_30" integer,
	"i060_40" integer,
	"i060_50" integer,
	"i060_60" integer,
	"i060_70" integer,
	"i060_80" integer,
	"i060_90" integer,
	"i080_10" integer,
	"i080_20" integer,
	"i080_30" integer,
	"i080_40" integer,
	"i080_50" integer,
	"i080_60" integer,
	"i080_70" integer,
	"i080_80" integer,
	"i080_90" integer,
	"i100_10" integer,
	"i100_20" integer,
	"i100_30" integer,
	"i100_40" integer,
	"i100_50" integer,
	"i100_60" integer,
	"i100_70" integer,
	"i100_80" integer,
	"i100_90" integer,
	"i120_10" integer,
	"i120_20" integer,
	"i120_30" integer,
	"i120_40" integer,
	"i120_50" integer,
	"i120_60" integer,
	"i120_70" integer,
	"i120_80" integer,
	"i120_90" integer,
	"i140_10" integer,
	"i140_20" integer,
	"i140_30" integer,
	"i140_40" integer,
	"i140_50" integer,
	"i140_60" integer,
	"i140_70" integer,
	"i140_80" integer,
	"i140_90" integer,
	"i160_10" integer,
	"i160_20" integer,
	"i160_30" integer,
	"i160_40" integer,
	"i160_50" integer,
	"i160_60" integer,
	"i160_70" integer,
	"i160_80" integer,
	"i160_90" integer,
	"i180_10" integer,
	"i180_20" integer,
	"i180_30" integer,
	"i180_40" integer,
	"i180_50" integer,
	"i180_60" integer,
	"i180_70" integer,
	"i180_80" integer,
	"i180_90" integer,
	"i200_10" integer,
	"i200_20" integer,
	"i200_30" integer,
	"i200_40" integer,
	"i200_50" integer,
	"i200_60" integer,
	"i200_70" integer,
	"i200_80" integer,
	"i200_90" integer,
	"i220_10" integer,
	"i220_20" integer,
	"i220_30" integer,
	"i220_40" integer,
	"i220_50" integer,
	"i220_60" integer,
	"i220_70" integer,
	"i220_80" integer,
	"i220_90" integer,
	"i240_10" integer,
	"i240_20" integer,
	"i240_30" integer,
	"i240_40" integer,
	"i240_50" integer,
	"i240_60" integer,
	"i240_70" integer,
	"i240_80" integer,
	"i240_90" integer,
	"i260_10" integer,
	"i260_20" integer,
	"i260_30" integer,
	"i260_40" integer,
	"i260_50" integer,
	"i260_60" integer,
	"i260_70" integer,
	"i260_80" integer,
	"i260_90" integer,
	"i280_10" integer,
	"i280_20" integer,
	"i280_30" integer,
	"i280_40" integer,
	"i280_50" integer,
	"i280_60" integer,
	"i280_70" integer,
	"i280_80" integer,
	"i280_90" integer,
	"i300_10" integer,
	"i300_20" integer,
	"i300_30" integer,
	"i300_40" integer,
	"i300_50" integer,
	"i300_60" integer,
	"i300_70" integer,
	"i300_80" integer,
	"i300_90" integer,
	"i320_10" integer,
	"i320_20" integer,
	"i320_30" integer,
	"i320_40" integer,
	"i320_50" integer,
	"i320_60" integer,
	"i320_70" integer,
	"i320_80" integer,
	"i320_90" integer,
	"i340_10" integer,
	"i340_20" integer,
	"i340_30" integer,
	"i340_40" integer,
	"i340_50" integer,
	"i340_60" integer,
	"i340_70" integer,
	"i340_80" integer,
	"i340_90" integer);

 
BEGIN;
INSERT INTO "gr_sonne"."irradiation" ("id", "x", "y", "ixxx_00", "i000_10", "i000_20", "i000_30", "i000_40", "i000_50", "i000_60", "i000_70", "i000_80", "i000_90", "i020_10", "i020_20", "i020_30", "i020_40", "i020_50", "i020_60", "i020_70", "i020_80", "i020_90", "i040_10", "i040_20", "i040_30", "i040_40", "i040_50", "i040_60", "i040_70", "i040_80", "i040_90", "i060_10", "i060_20", "i060_30", "i060_40", "i060_50", "i060_60", "i060_70", "i060_80", "i060_90", "i080_10", "i080_20", "i080_30", "i080_40", "i080_50", "i080_60", "i080_70", "i080_80", "i080_90", "i100_10", "i100_20", "i100_30", "i100_40", "i100_50", "i100_60", "i100_70", "i100_80", "i100_90", "i120_10", "i120_20", "i120_30", "i120_40", "i120_50", "i120_60", "i120_70", "i120_80", "i120_90", "i140_10", "i140_20", "i140_30", "i140_40", "i140_50", "i140_60", "i140_70", "i140_80", "i140_90", "i160_10", "i160_20", "i160_30", "i160_40", "i160_50", "i160_60", "i160_70", "i160_80", "i160_90", "i180_10", "i180_20", "i180_30", "i180_40", "i180_50", "i180_60", "i180_70", "i180_80", "i180_90", "i200_10", "i200_20", "i200_30", "i200_40", "i200_50", "i200_60", "i200_70", "i200_80", "i200_90", "i220_10", "i220_20", "i220_30", "i220_40", "i220_50", "i220_60", "i220_70", "i220_80", "i220_90", "i240_10", "i240_20", "i240_30", "i240_40", "i240_50", "i240_60", "i240_70", "i240_80", "i240_90", "i260_10", "i260_20", "i260_30", "i260_40", "i260_50", "i260_60", "i260_70", "i260_80", "i260_90", "i280_10", "i280_20", "i280_30", "i280_40", "i280_50", "i280_60", "i280_70", "i280_80", "i280_90", "i300_10", "i300_20", "i300_30", "i300_40", "i300_50", "i300_60", "i300_70", "i300_80", "i300_90", "i320_10", "i320_20", "i320_30", "i320_40", "i320_50", "i320_60", "i320_70", "i320_80", "i320_90", "i340_10", "i340_20", "i340_30", "i340_40", "i340_50", "i340_60", "i340_70", "i340_80", "i340_90") VALUES ('180981', '740050', '184950', '1384', '1240', '1072', '912', '761', '622', '499', '402', '342', '301', '1249', '1094', '942', '799', '668', '553', '470', '405', '357', '1272', '1144', '1014', '892', '785', '693', '610', '534', '469', '1307', '1215', '1122', '1032', '945', '859', '773', '686', '605', '1349', '1299', '1242', '1180', '1110', '1031', '943', '845', '749', '1393', '1384', '1360', '1321', '1264', '1189', '1098', '991', '879', '1436', '1462', '1465', '1443', '1396', '1323', '1226', '1109', '982', '1471', '1527', '1550', '1541', '1499', '1425', '1322', '1194', '1051', '1494', '1572', '1608', '1605', '1566', '1490', '1381', '1243', '1087', '1502', '1590', '1630', '1630', '1592', '1516', '1405', '1263', '1102', '1494', '1575', '1614', '1615', '1579', '1507', '1400', '1264', '1108', '1472', '1533', '1561', '1556', '1518', '1448', '1348', '1221', '1080', '1438', '1469', '1476', '1457', '1412', '1340', '1245', '1129', '1002', '1395', '1387', '1365', '1326', '1270', '1196', '1104', '997', '886', '1349', '1297', '1240', '1177', '1106', '1026', '937', '839', '742', '1305', '1209', '1113', '1020', '930', '842', '753', '664', '583', '1269', '1135', '999', '872', '761', '665', '579', '501', '436', '1246', '1085', '927', '780', '644', '526', '442', '376', '328');
COMMIT;

--
-- end SQL dump
--
