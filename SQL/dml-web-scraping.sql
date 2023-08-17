DROP DATABASE IF EXISTS IIDDBDWorldFactbook;

CREATE DATABASE IIDDBDWorldFactbook CHARACTER SET utf8mb4;

USE IIDDBDWorldFactbook;

CREATE TABLE Countries (
    id SERIAL PRIMARY KEY,
    tex_name VARCHAR(60) NOT NULL UNIQUE COMMENT "Nombre de país",
    dec_population DECIMAL(20,5) NOT NULL COMMENT "Cantidad de habitantes",
    dec_population_growth_percent DECIMAL(30,5) NOT NULL COMMENT "Porcentaje de crecimiento poblacional",
    dec_area_km_sq DECIMAL(20,5) NOT NULL COMMENT "Área en km cuadrados",
    tex_map_references VARCHAR(100) NOT NULL COMMENT "Referencias del país",
    int_coastline_km_sq INT NOT NULL COMMENT "ÁREA DE LÍNEA COSTERA",
    int_max_elevation_km INT NOT NULL COMMENT "Elevación máxima",
    int_min_elevation_km INT NOT NULL COMMENT "Punto más bajo del país",
    dec_population_density DECIMAL(20,5) NOT NULL COMMENT "Densidad poblacional"
) COMMENT "Datos generales del país";

CREATE TABLE Economy (
    id SERIAL PRIMARY KEY,
    id_countries_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    dec_GDP_general_billion_of_dollars DECIMAL(30,5) NOT NULL COMMENT "PIB PAÍS",
    dec_GDP_contribution_agriculture_percent DECIMAL(20,5) NOT NULL COMMENT "Aporte de agricultura al PIB",
    dec_GDP_contribution_industry_percent DECIMAL(20,5) NOT NULL COMMENT "Aporte de industria al PIB",
    dec_GDP_contribution_service_percent DECIMAL(20,5) NOT NULL COMMENT "Aporte de servicios al PIB",
    FOREIGN KEY (id_countries_fk) REFERENCES Countries(id) ON DELETE CASCADE
) COMMENT "Datos de la economía del país";

CREATE TABLE Education (
    id SERIAL PRIMARY KEY,
    id_countries_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    int_school_life_time INT NOT NULL COMMENT "Tiempo en que la persona está en la escuela",
    dec_education_cost_percent_GDP DECIMAL NOT NULL COMMENT "Costo en PIB de la educación",
    FOREIGN KEY (id_countries_fk) REFERENCES Countries(id) ON DELETE CASCADE
) COMMENT "Datos de la educación del país";

CREATE TABLE Health (
    id SERIAL PRIMARY KEY,
    id_countries_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia countries",
    int_life_expectancy_years INT NOT NULL COMMENT "Tiempo de vida esperado",
    int_infant_mortality_deathover1000births INT NOT NULL COMMENT "Tasa de mortalidad infantil",
    FOREIGN KEY (id_countries_fk) REFERENCES Countries(id) ON DELETE CASCADE
) COMMENT "Datos de la Salud del país";

CREATE TABLE HealthProblems (
    id SERIAL PRIMARY KEY,
    id_health_fk BIGINT UNSIGNED NOT NULL COMMENT "Referencia hacia health",
    dec_health_expenses_percent_GDP DECIMAL NOT NULL COMMENT "Costo de salud al PIB",
    int_physicians_over1000population INT NOT NULL COMMENT "Médicos cada mil personas",
    int_hospitalbeds_density_bedsover1000population INT NOT NULL COMMENT "Camas de hospital cada mil personas",
    FOREIGN KEY (id_health_fk) REFERENCES Health(id) ON DELETE CASCADE
) COMMENT "Datos de los problemas de Salud del país";