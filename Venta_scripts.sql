USE [Venta]
GO

/****** Object:  Table [dbo].[Ventas]    Script Date: 07/02/2026 19:27:00 ******/
SET ANSI_NULLS ON
GO

SET QUOTED_IDENTIFIER ON
GO

CREATE TABLE [dbo].[Ventas](
	[IdFactura] [varchar](10) NOT NULL,
	[IdCliente] [varchar](10) NULL,
	[NombreCLiente] [varchar](60) NULL,
	[ApellidoCLiente] [varchar](60) NULL,
	[IdProducto] [varchar](10) NULL,
	[NombreProducto] [varchar](60) NULL,
	[PrecioProducto] [decimal](7, 2) NULL,
	[Unidades] [int] NULL,
	[Subtotal] [decimal](7, 2) NULL,
	[Total] [decimal](7, 2) NULL,
 CONSTRAINT [PK__Ventas__50E7BAF104A28644] PRIMARY KEY CLUSTERED 
(
	[IdFactura] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON, OPTIMIZE_FOR_SEQUENTIAL_KEY = OFF) ON [PRIMARY]
) ON [PRIMARY]
GO

