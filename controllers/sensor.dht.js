/*
Author: Henry Cabral

*/

import pkg from 'node-dht-sensor';
const { promises: sensor } = pkg;

async function ambientread() {
    try {
        const res = await sensor.read(22, 4); // Type: DHT22, GPIO PinL 4
        console.log(
            `temperature: ${res.temperature.toFixed(1)}°C, ` +
                `humidity: ${res.humidity.toFixed(1)}%`
        );
    } catch (err) {
        console.error("Failure: Cannot read sensor data:", err);
    }
}

ambientread();