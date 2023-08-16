/*
    @author1 Alex Fuentes
    @author2 Yaser Rivera
    @version 0.01
    @since 2023-08-13
*/

DROP DATABASE IF EXISTS IIDDBDWorldFactbook;

CREATE DATABASE IIDDBDWorldFactbook CHARACTER SET utf8;

USE IIDDBDWorldFactbook;

CREATE TABLE Countries(
    id SERIAL PRIMARY KEY,
    tex_name VARCHAR(60) NOT NULL UNIQUE COMMENT "Nombre de pais",
    int_population INT NOT NULL COMMENT "Cantidad de habitantes",
    dec_population_growth_percent DECIMAL(10,2) NOT NULL COMMENT "Porcentaje de crecimiento poblacional",
    int_area_km_sq INT NOT NULL COMMENT "Area en km cuadrados",
    tex_map_references VARCHAR(100) NOT NULL COMMENT "Referencias del pais",
    int_coastline_km INT NOT NULL COMMENT "Linea costera",
    int_max_elevation_km INT NOT NULL COMMENT "Elevacion maxima",
    int_min_elevation_km INT NOT NULL COMMENT "Punto mas bajo pais",
    dec_population_density DECIMAL(10,2) NOT NULL COMMENT "Densidad poblacional",
) COMMENT "Datos generales del pais";

CREATE TABLE Economy(
    id SERIAL PRIMARY KEY,
    id_coutries_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    int_GDP_general_billion_of_dollars INT NOT NULL COMMENT "PIB",
    dec_GDP_contribution_agriculture_percent DECIMAL(10,2) NOT NULL COMMENT "Aporte de agricultura al PIB",
    dec_GDP_contribution_industry_percent DECIMAL(10,2) NOT NULL COMMENT "Aporte de industria al PIB",
    dec_GDP_contribution_service_percent DECIMAL(10,2) NOT NULL COMMENT "Aporte de servicios al PIB",
    FOREIGN KEY (id_coutries_fk) REFERENCES Countries(id) ON DELETE CASCADE
) COMMENT "Datos de la economia del pais";

CREATE TABLE Education(
    id SERIAL PRIMARY KEY,
    id_coutries_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    int_school_life_time INT NOT NULL COMMENT "Tiempo en que la persona esta en la escuela",
    dec_education_cost_percent_GDP DECIMAL NOT NULL COMMENT "Costo en PIB de la educacion",
    FOREIGN KEY (id_coutries_fk) REFERENCES Countries(id) ON DELETE CASCADE
) COMMENT "Datos de la educacion del pais";

CREATE TABLE Health(
    id SERIAL PRIMARY KEY,
    id_coutries_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    int_life_expectancy_years INT NOT NOT NULL COMMENT "Tiempo de vida esperado",
    int_infant_mortality_deathover1000births INT NOT NOT NULL COMMENT "Tasa de mortalidad infantil",
    FOREIGN KEY (id_coutries_fk) REFERENCES Countries(id) ON DELETE CASCADE
) COMMENT "Datos de la Salud del pais";

CREATE TABLE HealhtProblems(
    id SERIAL PRIMARY KEY,
    id_health_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    dec_health_expenses_PercenteGDP DECIMAL NOT NULL COMMENT "costo de salud al PIB",
    int_physicians_over1000population INT NOT NOT NULL COMMENT "medicos cada mil personas",
    int_hospitalbeds_density_bedsover1000population INT NOT NOT NULL COMMENT "Camas de hospital cada mil personas",
    FOREIGN KEY (id_health_fk) REFERENCES Health(id) ON DELETE CASCADE
) COMMENT "Datos de los problemas de Salud del pais";