set -e
SQLITEFILE=$1
OUTPUTDIR=`dirname $SQLITEFILE`
NOW=$(date +"%Y%m%d-%H%M%S")
DB='spatial_data'
CSVFILE=/tmp/GRsonne$RANDOM.csv
PGDUMPFILE=GRsonne-$NOW.pgdump
echo "Creating temporary file $CSVFILE..."

#sqlite3 -header -csv $SQLITEFILE "select id, x, y, Ixxx_0, I000_1, I000_2, I000_3, I000_4, I000_5, I000_6, I000_7, I000_8, I000_9, I020_1, I020_2, I020_3, I020_4, I020_5, I020_6, I020_7, I020_8, I020_9, I040_1, I040_2, I040_3, I040_4, I040_5, I040_6, I040_7, I040_8, I040_9, I060_1, I060_2, I060_3, I060_4, I060_5, I060_6, I060_7, I060_8, I060_9, I080_1, I080_2, I080_3, I080_4, I080_5, I080_6, I080_7, I080_8, I080_9, I100_1, I100_2, I100_3, I100_4, I100_5, I100_6, I100_7, I100_8, I100_9, I120_1, I120_2, I120_3, I120_4, I120_5, I120_6, I120_7, I120_8, I120_9, I140_1, I140_2, I140_3, I140_4, I140_5, I140_6, I140_7, I140_8, I140_9, I160_1, I160_2, I160_3, I160_4, I160_5, I160_6, I160_7, I160_8, I160_9, I180_1, I180_2, I180_3, I180_4, I180_5, I180_6, I180_7, I180_8, I180_9, I200_1, I200_2, I200_3, I200_4, I200_5, I200_6, I200_7, I200_8, I200_9, I220_1, I220_2, I220_3, I220_4, I220_5, I220_6, I220_7, I220_8, I220_9, I240_1, I240_2, I240_3, I240_4, I240_5, I240_6, I240_7, I240_8, I240_9, I260_1, I260_2, I260_3, I260_4, I260_5, I260_6, I260_7, I260_8, I260_9, I280_1, I280_2, I280_3, I280_4, I280_5, I280_6, I280_7, I280_8, I280_9, I300_1, I300_2, I300_3, I300_4, I300_5, I300_6, I300_7, I300_8, I300_9, I320_1, I320_2, I320_3, I320_4, I320_5, I320_6, I320_7, I320_8, I320_9, I340_1, I340_2, I340_3, I340_4, I340_5, I340_6, I340_7, I340_8, I340_9 from irradiation;" > $CSVFILE


# uncomment this for the new naming
sqlite3 -header -csv $SQLITEFILE "select OGC_FID, x, y, ixxx_00, i000_10, i000_20, i000_30, i000_40, i000_50, i000_60, i000_70, i000_80, i000_90, i020_10, i020_20, i020_30, i020_40, i020_50, i020_60, i020_70, i020_80, i020_90, i040_10, i040_20, i040_30, i040_40, i040_50, i040_60, i040_70, i040_80, i040_90, i060_10, i060_20, i060_30, i060_40, i060_50, i060_60, i060_70, i060_80, i060_90, i080_10, i080_20, i080_30, i080_40, i080_50, i080_60, i080_70, i080_80, i080_90, i100_10, i100_20, i100_30, i100_40, i100_50, i100_60, i100_70, i100_80, i100_90, i120_10, i120_20, i120_30, i120_40, i120_50, i120_60, i120_70, i120_80, i120_90, i140_10, i140_20, i140_30, i140_40, i140_50, i140_60, i140_70, i140_80, i140_90, i160_10, i160_20, i160_30, i160_40, i160_50, i160_60, i160_70, i160_80, i160_90, i180_10, i180_20, i180_30, i180_40, i180_50, i180_60, i180_70, i180_80, i180_90, i200_10, i200_20, i200_30, i200_40, i200_50, i200_60, i200_70, i200_80, i200_90, i220_10, i220_20, i220_30, i220_40, i220_50, i220_60, i220_70, i220_80, i220_90, i240_10, i240_20, i240_30, i240_40, i240_50, i240_60, i240_70, i240_80, i240_90, i260_10, i260_20, i260_30, i260_40, i260_50, i260_60, i260_70, i260_80, i260_90, i280_10, i280_20, i280_30, i280_40, i280_50, i280_60, i280_70, i280_80, i280_90, i300_10, i300_20, i300_30, i300_40, i300_50, i300_60, i300_70, i300_80, i300_90, i320_10, i320_20, i320_30, i320_40, i320_50, i320_60, i320_70, i320_80, i320_90, i340_10, i340_20, i340_30, i340_40, i340_50, i340_60, i340_70, i340_80, i340_90 from irradiation;" > $CSVFILE


######################################################################
##################### MANUAL VERSION #################################
######################################################################
#echo
#echo "export completed at $CSVFILE, you now have 2 options."
#echo
#echo 'Run the following comand In pgadmin or similar:'
#echo
#echo '-----------START COPY/PASTE-------------'
#sed ':a;N;$!ba;s/[\t\n]/ /g' create_table.sql
#echo COPY gr_sonne.irradiation FROM \'$CSVFILE\' DELIMITER \',\' CSV HEADER\;
#echo '-----------END COPY/PASTE-------------'
#echo 
#echo 'OR'
#echo
#echo 'Run the following in the comand line:'
#echo psql -d $DB -a -f create_table.sql
#echo 'psql -d '$DB' -c "COPY gr_sonne.irradiation FROM '\'$CSVFILE\'' DELIMITER '\',\'' CSV HEADER;"'
#echo 'pg_dump --schema=gr_sonne' $DB \> $PGDUMPFILE



######################################################################
##################### AUTOMATIC VERSION ##############################
######################################################################
echo "Recreating postgress DB..."
psql -d $DB -c "DROP TABLE IF EXISTS gr_sonne.irradiation"
psql -d $DB -a -f create_table.sql
echo "dumping postgress DB..."
psql -d $DB -c "COPY gr_sonne.irradiation FROM '$CSVFILE' DELIMITER ',' CSV HEADER;"
pg_dump --schema=gr_sonne $DB > $PGDUMPFILE

tar -C $OUTPUTDIR -czf $PGDUMPFILE.tar.gz $PGDUMPFILE
rm -f $PGDUMPFILE
rm -f $CSVFILE
echo "Dumped to "$(readlink -f $OUTPUTDIR/$PGDUMPFILE.tar.gz)

