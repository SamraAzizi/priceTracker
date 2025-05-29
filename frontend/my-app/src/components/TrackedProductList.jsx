import React, { useState, useEffect } from "react";
import axios from "axios";

const TrackedProductList = () => {
  const [trackedProducts, setTrackedProducts] = useState([]);
  const [newTrackedProduct, setNewTrackedProduct] = useState("");

  useEffect(() => {
    fetchTrackedProducts();
  }, []);

  const fetchTrackedProducts = async () => {
    try {
      const response = await axios.get(
        "http://localhost:5000/tracked-products"
      );