-- phpMyAdmin SQL Dump
-- version 5.0.1
-- https://www.phpmyadmin.net/
--
-- Servidor: 127.0.0.1
-- Tiempo de generación: 17-04-2020 a las 10:10:41
-- Versión del servidor: 10.4.11-MariaDB
-- Versión de PHP: 7.4.3

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
SET AUTOCOMMIT = 0;
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `db_musical`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_canciones`
--

CREATE TABLE `tabla_canciones` (
  `ID` int(11) NOT NULL,
  `TITULO` varchar(255) NOT NULL,
  `ARTISTA` varchar(255) NOT NULL,
  `ALBUM` varchar(255) NOT NULL,
  `AÑO` int(4) NOT NULL,
  `ESTILO` varchar(255) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_canciones`
--

INSERT INTO `tabla_canciones` (`ID`, `TITULO`, `ARTISTA`, `ALBUM`, `AÑO`, `ESTILO`) VALUES
(1, 'El roce de tu cuerpo', 'Platero y Tú', 'Muy deficiente', 1992, 'Rock Español'),
(2, 'Thunderstruck', 'AC/DC', 'Live At Donington', 1990, 'Hard Rock'),
(3, 'Faded', 'Alan Walker', 'Faded', 0, 'Electro House'),
(4, 'Wonderwall', 'Oasis', '(What\'s the Story) Morning Glory?', 1995, 'Pop Británico'),
(5, 'Corazón de mimbre', 'Marea', 'Revolcón', 2000, 'Rock Español'),
(21, 'Por verte sonreir', 'La Fuga', 'Un juguete por navidad', 1998, 'Rock Español'),
(24, 'Buscando en la basura', 'La fuga', 'Negociando gasolina', 2005, 'Rock Español'),
(27, 'ghost Buster', 'los cazafantasmas', 'Los cazafantasmas', 0, 'Bso'),
(29, 'Merezca la pena', 'La ley de Mantua', 'Calma', 2010, 'Pop'),
(30, 'Billy Joe', 'Dinamita para los pollos', 'LOs mejores años de nuestra vida', 1990, 'Pop'),
(31, 'Reina Magreb', 'La ley de Mantua', 'Calma', 2010, 'Pop'),
(32, 'No solo respirar', 'La fuga', 'asuntos pendientes', 2009, 'Rock');

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `tabla_usuarios`
--

CREATE TABLE `tabla_usuarios` (
  `ID` int(11) NOT NULL,
  `USUARIO` varchar(40) NOT NULL,
  `EMAIL` varchar(60) NOT NULL,
  `NEWSLETTER` varchar(2) NOT NULL,
  `EVENTOS` varchar(2) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `tabla_usuarios`
--

INSERT INTO `tabla_usuarios` (`ID`, `USUARIO`, `EMAIL`, `NEWSLETTER`, `EVENTOS`) VALUES
(1, 'silvi sil', 'silvita@gmail.com', 'Si', 'No'),
(3, 'LucasThor', 'luqitas@yahoo.es', 'No', 'Si'),
(4, 'María_2', 'mariirta@hotmail.com', 'No', 'Si'),
(5, 'Antonio', 'aaf@gmail.com', 'Si', 'No'),
(6, 'Carmen', 'carmencita@hotmail.com', 'Si', 'Si'),
(7, 'Pedro', 'pedrito@gmail.com', 'No', 'No'),
(8, 'Juana', 'la_juanita@terra.es', 'Si', 'Si'),
(9, 'Carlos', 'carlitos@gmail.com', 'Si', 'Si'),
(10, 'maribel', 'maribel@gmail.com', 'Si', 'Si'),
(11, 'caracola', 'holahola#gmail.com', 'Si', 'No'),
(12, 'bebte2', 'bebtetes@gmail.com', 'Si', 'Si'),
(13, 'Silvia', 'hola@gomail.com', 'Si', 'Si');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `tabla_canciones`
--
ALTER TABLE `tabla_canciones`
  ADD PRIMARY KEY (`ID`);

--
-- Indices de la tabla `tabla_usuarios`
--
ALTER TABLE `tabla_usuarios`
  ADD PRIMARY KEY (`ID`);

--
-- AUTO_INCREMENT de las tablas volcadas
--

--
-- AUTO_INCREMENT de la tabla `tabla_canciones`
--
ALTER TABLE `tabla_canciones`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=33;

--
-- AUTO_INCREMENT de la tabla `tabla_usuarios`
--
ALTER TABLE `tabla_usuarios`
  MODIFY `ID` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=14;
COMMIT;

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
