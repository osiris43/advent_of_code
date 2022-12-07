(ns rock-paper-scissors.solver
  (:require [clojure.string :as str]))

(def scoring {"AX" 4
              "AY" 8
              "AZ" 3
              "BX" 1
              "BY" 5
              "BZ" 9
              "CX" 7
              "CY" 2
              "CZ" 6})

(def ->strategy {"AY" "AX"
                 "AX" "AZ"
                 "AZ" "AY"
                 "BX" "BX"
                 "BY" "BY"
                 "BZ" "BZ"
                 "CX" "CY"
                 "CY" "CZ"
                 "CZ" "CX"})

(defn get-input [f]
  (slurp f))

(let [[f] *command-line-args*]
  (when (empty? f)
    (println "Usage: enter a file to process")
    (System/exit 1))
  (let [strategy (str/split-lines (get-input f))]
    (->> strategy
         (map #(str/replace % " " ""))
         (map #(get ->strategy %)) ;; comment out for problem 1
         (map #(get scoring %))
         (reduce +)
         (println))))