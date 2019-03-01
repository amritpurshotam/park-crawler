CREATE TABLE [dbo].[Countries]
(
	[CountryId] INT NOT NULL IDENTITY(1,1),
	[Name] VARCHAR(100),
	[BaseUrl] VARCHAR(100),
	[Latitude] DECIMAL(9,6) NOT NULL,
	[Longitude] DECIMAL(9,6) NOT NULL,
	CONSTRAINT [PK_Countries] PRIMARY KEY CLUSTERED ([CountryId] ASC)
)

CREATE TABLE [dbo].[Regions]
(
	[RegionId] INT NOT NULL IDENTITY(1,1),
	[CountryId] INT NOT NULL,
	[Name] VARCHAR(100),
	[Latitude] DECIMAL(9,6) NOT NULL,
	[Longitude] DECIMAL(9,6) NOT NULL,
	CONSTRAINT [PK_Regions] PRIMARY KEY CLUSTERED ([RegionId] ASC),
	CONSTRAINT [FK_Regions_Countries] FOREIGN KEY ([CountryId]) REFERENCES [dbo].[Countries] ([CountryId])
)

CREATE TABLE [dbo].[Courses]
(
	[CourseId] INT NOT NULL IDENTITY(1,1),
	[RegionId] INT NOT NULL,
	[Name] VARCHAR(100) NOT NULL,
	[Url] VARCHAR(200) NOT NULL,
	[Latitude] DECIMAL(9,6) NOT NULL,
	[Longitude] DECIMAL(9,6) NOT NULL,
	[Description] VARCHAR(2000) NOT NULL,
	CONSTRAINT [PK_Courses] PRIMARY KEY CLUSTERED ([CourseId] ASC),
	CONSTRAINT [FK_Courses_Regions] FOREIGN KEY ([RegionId]) REFERENCES [dbo].[Regions] ([RegionId])
)

CREATE TABLE [dbo].[Events]
(
	[EventId] INT NOT NULL IDENTITY(1,1),
	[CourseId] INT NOT NULL,
	[RunSequenceNumber] INT NOT NULL,
	[Date] DATETIME NOT NULL,
	CONSTRAINT [PK_Events] PRIMARY KEY CLUSTERED ([EventId] ASC),
	CONSTRAINT [FK_Events_Courses] FOREIGN KEY ([EventId]) REFERENCES [dbo].[Courses] ([CourseId])
)

CREATE TABLE [dbo].[Runs]
(
	[RunId] INT NOT NULL IDENTITY(1,1),
	[EventId] INT NOT NULL,
	[ParkRunnerId] INT NOT NULL,
	[Position] INT NOT NULL,
	[Hours] INT NOT NULL,
	[Minutes] INT NOT NULL,
	[Seconds] INT NOT NULL,
	[AgeCategory] CHAR(2) NOT NULL,
	[AgeMin] INT NOT NULL,
	[AgeMax] INT NOT NULL,
	[AgeGrade] DECIMAL(4,2) NOT NULL,
	[Gender] CHAR(1) NOT NULL, 
	[GenderPosition] INT NULL,
	CONSTRAINT [PK_Runs] PRIMARY KEY CLUSTERED ([RunId] ASC),
	CONSTRAINT [FK_Runs_Events] FOREIGN KEY ([EventId]) REFERENCES [dbo].[Events] ([EventId])
)