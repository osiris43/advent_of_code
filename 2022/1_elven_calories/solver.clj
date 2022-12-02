(ns solver
  (:require [clojure.string :as str]))

(defn get-input [f]
  (slurp f))

(defn sum-calories [foods]
  (->> foods
       (map #(Integer/parseInt %))
       (reduce +)))

(let [[f] *command-line-args*]
  (when (empty? f)
    (println "Usage: enter a file to process")
    (System/exit 1))
  (let [elves (str/split-lines (get-input f))]
    (->> elves
         (partition-by #(= "" %))
         (filter #(not (= "" (first %))))
         (map sum-calories)
         (map-indexed vector)
         ;;(apply max-key second)
         (sort-by second)
         (take-last 3)
         (println))))