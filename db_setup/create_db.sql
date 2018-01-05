
-- Create schema from C:\Users\assen_bankov\Documents\GitHub\Flask_MyFirstApp\db_setup\aceh40db_schema.xml

CREATE TABLE "User" (
"userId"  SERIAL ,
"email" VARCHAR(100) NOT NULL ,
"password_hash" VARCHAR(200) NOT NULL ,
"firstName" VARCHAR(20) ,
"lastName" VARCHAR(50) ,
"activeFlag" BOOLEAN NOT NULL DEFAULT '1' ,
"registeredDate" TIMESTAMP WITHOUT TIME ZONE ,
PRIMARY KEY ("userId")
);
COMMENT ON TABLE "User" IS 'Lists all registered users';

CREATE TABLE "ActivityLog" (
"activityLogId"  SERIAL ,
"userId" INTEGER NOT NULL ,
"activityId" INTEGER ,
"effectiveDate" TIMESTAMP WITHOUT TIME ZONE NOT NULL ,
"numerical" DECIMAL ,
"notes" TEXT ,
"completed" BOOLEAN ,
PRIMARY KEY ("activityLogId")
);
COMMENT ON TABLE "ActivityLog" IS 'Log different activities';

CREATE TABLE "ActivityType" (
"activityTypeId"  SERIAL ,
"activityName" VARCHAR(100) ,
"description" TEXT ,
"activeFlag" BOOLEAN DEFAULT '1',
"isHabit" BOOLEAN DEFAULT '0',
PRIMARY KEY ("activityTypeId")
);
COMMENT ON TABLE "ActivityType" IS 'List of all activity types';

CREATE TABLE "Parkour" (
"parkourId"  SERIAL ,
"parkourName" VARCHAR(100) NOT NULL ,
"diagram" INET ,
PRIMARY KEY ("parkourId")
);
COMMENT ON TABLE "Parkour" IS 'list of all parkours';

CREATE TABLE "TennisString" (
"stringId"  SERIAL ,
"stringMake" VARCHAR(50) ,
"stringModel" VARCHAR(150) ,
"gauge" VARCHAR(10) ,
"stringType" INTEGER ,
PRIMARY KEY ("stringId")
);
COMMENT ON TABLE "TennisString" IS 'list of tennis strings';

CREATE TABLE "StringType" (
"stringTypeId"  SERIAL ,
"stringTypeName" VARCHAR(20) NOT NULL ,
"stringForumUrl" VARCHAR(200) ,
"vendorUrl" VARCHAR(500) ,
PRIMARY KEY ("stringTypeId")
);
COMMENT ON TABLE "StringType" IS 'list of string types';

CREATE TABLE "TennisRacquet" (
"racquetId"  SERIAL ,
"racquetMake" VARCHAR(20) ,
"racquetModel" VARCHAR(100) ,
PRIMARY KEY ("racquetId")
);

CREATE TABLE "TennisRacquetSpec" (
"racquetSpecId"  SERIAL ,
"racquetId" INTEGER ,
"specId" INTEGER ,
"specValue" DECIMAL ,
"specTxtValue" TEXT ,
PRIMARY KEY ("racquetSpecId")
);
COMMENT ON TABLE "TennisRacquetSpec" IS 'Lists all specs of a racquet (head size, swingweight etc.)';

CREATE TABLE "RacquetSpecType" (
"specId"  SERIAL ,
"specName" VARCHAR(50) ,
"specMeasure" VARCHAR(20) ,
PRIMARY KEY ("specId")
);
COMMENT ON TABLE "RacquetSpecType" IS 'Lists data items for tennis racquet specs';

CREATE TABLE "RacquetStringJob" (
"stringJobId"  SERIAL ,
"racquetId" INTEGER ,
"mainsStringId" INTEGER ,
"mainsTension_lb" DECIMAL ,
"crossStringId" INTEGER ,
"crossTension_lb" DECIMAL ,
"notes" TEXT ,
"effectiveDate" TIMESTAMP WITHOUT TIME ZONE ,
"toDate" TIMESTAMP WITHOUT TIME ZONE ,
PRIMARY KEY ("stringJobId")
);
COMMENT ON TABLE "RacquetStringJob" IS 'Lists all string jobs I have done ';

ALTER TABLE "ActivityLog" ADD FOREIGN KEY ("userId") REFERENCES "User" ("userId");
ALTER TABLE "ActivityLog" ADD FOREIGN KEY ("activityId") REFERENCES "ActivityType" ("activityTypeId");
ALTER TABLE "TennisString" ADD FOREIGN KEY ("stringType") REFERENCES "StringType" ("stringTypeId");
ALTER TABLE "TennisRacquetSpec" ADD FOREIGN KEY ("racquetId") REFERENCES "TennisRacquet" ("racquetId");
ALTER TABLE "TennisRacquetSpec" ADD FOREIGN KEY ("specId") REFERENCES "RacquetSpecType" ("specId");
ALTER TABLE "RacquetStringJob" ADD FOREIGN KEY ("racquetId") REFERENCES "TennisRacquet" ("racquetId");
ALTER TABLE "RacquetStringJob" ADD FOREIGN KEY ("mainsStringId") REFERENCES "TennisString" ("stringId");
ALTER TABLE "RacquetStringJob" ADD FOREIGN KEY ("crossStringId") REFERENCES "TennisString" ("stringId");