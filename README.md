# APIChallenge

# API Name: WeatherServiceAPI  
**Base URL:** `http://myteam:5000`

---

## Endpoints

### 1. `GET /getcities/`
- **Description:** Returns a list of supported city airport codes.
- **Parameters:** None
- **Response:** JSON with a list of available airport codes.
- **Example:**
  ```json
  {
    "airports": ["SBA", "SMX"]
  }
  ```

---

### 2. `GET /temperature/<city>`
- **Description:** Returns the temperature for the specified city.
- **Parameters:**
  - `city` (string): The airport code of the city (e.g., `SBA` or `SMX`)
- **Response:**
  - If valid: JSON with temperature in Fahrenheit
  - If invalid: Plain text `"Invalid Request"`
- **Example:**
  ```json
  {
    "temperature": "72"
  }
  ```

---

### 3. `GET /wind_speed/<city>`
- **Description:** Returns the wind speed and direction for the specified city.
- **Parameters:**
  - `city` (string): The airport code of the city (e.g., `SBA` or `SMX`)
- **Response:**
  - If valid: JSON with wind speed and direction
  - If invalid: Plain text `"Invalid Request"`
- **Example:**
  ```json
  {
    "speed": "2.2",
    "direction": "NW"
  }
  ```

---

### 4. `GET /cloud_cover/<city>`
- **Description:** Returns the cloud cover level for the specified city.
- **Parameters:**
  - `city` (string): The airport code of the city (e.g., `SBA` or `SMX`)
- **Response:**
  - If valid: JSON with cloud cover level
  - If invalid: Plain text `"Invalid Request"`
- **Example:**
  ```json
  {
    "cloud_cover": "2"
  }
  ```
