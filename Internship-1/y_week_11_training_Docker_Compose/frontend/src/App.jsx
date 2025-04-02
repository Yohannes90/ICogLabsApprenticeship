import { useState } from "react";
import { motion } from "framer-motion";

const featureLabels = [
  { name: "Buying Price", options: ["Very High", "High", "Medium", "Low"] },
  { name: "Maintenance Cost", options: ["Very High", "High", "Medium", "Low"] },
  { name: "Number of Doors", options: ["2", "3", "4", "5 or More"] },
  { name: "Seating Capacity", options: ["2", "4", "More"] },
  { name: "Luggage Boot Size", options: ["Big", "Medium", "Small"] },
  { name: "Safety Rating", options: ["High", "Medium", "Low"] },
];

const featureMapping = [
  { VeryHigh: 3, High: 0, Medium: 2, Low: 1 },
  { VeryHigh: 3, High: 0, Medium: 2, Low: 1 },
  { "2": 0, "3": 1, "4": 2, "5 or More": 3 },
  { "2": 0, "4": 1, More: 2 },
  { Big: 0, Medium: 1, Small: 2 },
  { High: 0, Medium: 2, Low: 1 },
];

function App() {
  const [features, setFeatures] = useState([3, 2, 2, 2, 0, 0]);
  const [prediction, setPrediction] = useState("");
  const [history, setHistory] = useState([]);
  const [carName, setCarName] = useState("");
  const [loading, setLoading] = useState(false);

  const handleChange = (index, value) => {
    const updatedFeatures = [...features];
    updatedFeatures[index] = featureMapping[index][value];
    setFeatures(updatedFeatures);
  };

  const handleSubmit = async () => {
    if (!carName) {
      alert("Please enter a car name!");
      return;
    }

    setLoading(true);
    const response = await fetch("http://localhost:8000/predict", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ features }),
      mode: "cors",
    });

    const data = await response.json();
    const predictionResult = data.prediction === "unacc" ? "Unacceptable" : "Acceptable";
    setPrediction(predictionResult);
    setLoading(false);

    // Store the history
    const newHistory = [
      ...history,
      { carName, prediction: predictionResult, features },
    ];
    setHistory(newHistory);
  };

  const clearHistory = () => {
    setHistory([]);
  };

  return (
    <div className="min-h-screen flex flex-col items-center justify-center bg-gradient-to-br from-gray-900 to-gray-800 text-white px-4">
      <motion.h1
        initial={{ opacity: 0, y: -20 }}
        animate={{ opacity: 1, y: 0 }}
        className="text-4xl font-extrabold text-cyan-400 mb-6 drop-shadow-lg"
      >
        🚗 AI Car Dealership Predictor 🚀
      </motion.h1>

      {/* Flex container for form and history table */}
      <div className="mt-8 w-full flex justify-center gap-8">
        {/* Left side: Form */}
        <div className="w-1/4 p-8 bg-gray-800/50 rounded-2xl shadow-2xl backdrop-blur-md border border-gray-700">
          <p className="text-lg text-gray-300 mb-6 text-center">
            Select car details to predict if it's a good buy!
          </p>

          <div className="grid grid-cols-1 gap-4">
            {/* Car Name Input */}
            <div>
              <label className="block text-sm font-semibold text-gray-400 mb-1">
                Car Name
              </label>
              <input
                type="text"
                className="w-full p-3 bg-gray-900 text-cyan-400 border border-cyan-500 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500 transition"
                placeholder="Enter car name"
                value={carName}
                onChange={(e) => setCarName(e.target.value)}
              />
            </div>

            {featureLabels.map((feature, index) => (
              <div key={index}>
                <label className="block text-sm font-semibold text-gray-400 mb-1">
                  {feature.name}
                </label>
                <select
                  className="w-full p-3 bg-gray-900 text-cyan-400 border border-cyan-500 rounded-lg focus:outline-none focus:ring-2 focus:ring-cyan-500 transition"
                  onChange={(e) => handleChange(index, e.target.value)}
                >
                  {feature.options.map((option, optIndex) => (
                    <option key={optIndex} value={option}>
                      {option}
                    </option>
                  ))}
                </select>
              </div>
            ))}
          </div>

          {/* Predict Button */}
          <motion.button
            whileHover={{ scale: 1.05 }}
            whileTap={{ scale: 0.95 }}
            className="mt-6 w-full bg-cyan-500 hover:bg-cyan-400 text-gray-900 font-bold py-3 rounded-lg transition shadow-lg"
            onClick={handleSubmit}
            disabled={loading}
          >
            {loading ? "Predicting..." : "🔍 Predict"}
          </motion.button>

          {/* Prediction Result */}
          {prediction && (
            <motion.div
              initial={{ opacity: 0, y: 20 }}
              animate={{ opacity: 1, y: 0 }}
              className="mt-6 p-6 bg-gray-800/50 rounded-xl text-2xl text-cyan-300 shadow-xl backdrop-blur-md border border-gray-700"
            >
              🚘 Prediction: <span className="font-bold">{prediction}</span>
            </motion.div>
          )}
        </div>

        <div className="w-2/4 p-6 bg-gray-800/3 rounded-xl shadow-lg border border-gray-700 overflow-x-auto flex flex-col">
          <h2 className="text-xl font-bold text-cyan-300 mb-4">Prediction History</h2>
          <div className="overflow-y-auto flex-grow">
            <table className="w-full table-auto text-left text-gray-300">
              <thead>
                <tr>
                  <th className="py-2 px-4 border-b border-gray-700">Car Name</th>
                  <th className="py-2 px-4 border-b border-gray-700">Prediction</th>
                  {featureLabels.map((feature, index) => (
                    <th key={index} className="py-2 px-4 border-b border-gray-700">
                      {feature.name}
                    </th>
                  ))}
                </tr>
              </thead>
              <tbody>
                {history.map((entry, index) => (
                  <tr key={index} className="border-b border-gray-700">
                    <td className="h-16 py-2 px-4">{entry.carName}</td> {/* Consistent height */}
                    <td className="h-16 py-2 px-4">{entry.prediction}</td> {/* Consistent height */}
                    {entry.features.map((featureValue, featureIndex) => (
                      <td key={featureIndex} className="h-16 py-2 px-4">
                        {
                          Object.keys(featureMapping[featureIndex]).find(
                            (key) => featureMapping[featureIndex][key] === featureValue
                          )
                        }
                      </td>
                    ))}
                  </tr>
                ))}
              </tbody>
            </table>
          </div>
          <button
            onClick={clearHistory}
            className="mt-4 w-full bg-red-500 hover:bg-red-400 text-gray-900 font-bold py-2 rounded-lg transition shadow-lg"
          >
            🗑️ Clear History
          </button>
        </div>

      </div>
    </div>
  );
}

export default App;



