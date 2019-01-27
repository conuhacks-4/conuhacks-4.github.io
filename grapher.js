var arr = new Array(365);
for(i=0;i<365;i++){
    arr[i]=i;
}

var layout1 = {
    title: {
      text:'Queen',
      font: {
        family: 'Courier New, monospace',
        size: 24
      },
    },
    xaxis: {
      title: {
        text: 'month of the year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'number of plays per day',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    }
  };
      
var trace1 = {
  x: arr,
  y: [1651,1489,1582,1590,2072,2243,1545,1542,1642,1737,1825,2093,2070,1749,26,11,1682,1865,2076,2390,1705,1639,1599,1697,1875,2134,2438,1846,1688,1590,1642,1868,2192,2462,1767,1750,1601,1684,1897,2134,2281,1765,1632,1646,1739,1887,2216,2346,1960,1669,1705,1785,1933,2171,2536,1958,1693,1666,1717,1872,2203,2483,1916,1727,1694,1805,1858,2112,2498,1893,1663,1629,1724,1784,1952,2470,1788,1649,1612,1731,1999,2124,2338,1870,1667,1645,1742,1996,2327,2242,1599,1666,1703,1704,1939,2203,2468,1843,1684,1644,1661,1784,2093,2445,1823,1605,1648,1638,1810,1964,35,20,1587,1653,1613,1771,2076,2191,1827,1585,1543,1576,1841,1996,2209,1795,1533,1573,1633,1740,2046,2119,1742,1560,1698,1607,1913,2192,2390,1945,1588,1586,1694,1897,2200,2216,1977,1809,1568,1608,1864,2135,2355,1771,1707,1702,1700,1941,2084,2288,1897,1684,1657,1633,1980,2154,2149,1780,1675,1646,1642,1856,2103,2200,1800,1597,1570,1707,1962,1984,2166,1824,1647,1835,1618,1766,2029,1972,1647,1574,1595,1583,1779,2045,2238,1759,1615,1661,1661,1822,2139,2246,1807,1682,1590,1663,1703,2051,2199,25,0,22,1699,1876,2146,2386,1845,1623,1739,1669,1713,2175,2353,1846,1627,1609,1679,1791,2088,2196,1889,1577,1616,1771,1837,2020,2238,1860,1533,1659,1806,1793,2123,2164,2055,1720,1554,1711,1795,2230,2230,1641,1458,1636,1819,1762,2095,2283,1652,1626,1757,1753,1837,2216,2328,1706,1521,1710,1735,1847,2222,2119,1524,1550,1668,1653,1803,2135,2308,1680,1647,1705,1827,1985,2291,2484,1781,1724,1713,1797,1955,2378,2420,1730,1696,1754,1841,2079,2389,2437,1843,1794,1942,2069,2478,3671,4074,2887,2382,41,0,50,3660,4086,3002,2451,2570,2655,2693,3568,3969,2772,2294,2556,3541,2291,3567,3746,2410,2156,2367,2467,2652,3409,3571,2429,2188,2383,2361,2510,3322,3574,2302,2086,2228,2445,2504,3170,3451,2495,2061,2276,2455,2703,3321,3259,2475,2145,1618,2406,2685,3160,3235,4831,3097],
  fill: 'tozeroy',
  type: 'scatter'
};
var data1 = [trace1];
Plotly.newPlot('myDiv1', data1, layout1);

var layout2 = {
    title: {
      text:'Queen',
      font: {
        family: 'Courier New, monospace',
        size: 24
      },
    },
    xaxis: {
      title: {
        text: 'month of the year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'sum of the number of plays',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    }
  };
      

var data2 = [{
  x: ['January', 'February', 'March', "April", "May", "June", "July", "August", "September", "October", "November", "December"],
  y: [52733, 53660, 60013, 51282, 56658, 56525, 50797, 57782, 55706, 60078, 80465, 84746],
  type: 'bar'
}];


Plotly.newPlot('myDiv2', data2, layout2, {}, {showSendToCloud:true});

var data3 = [{
    x: ['January', 'February', 'March', "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    y: [5578,5885,6769,5262,6059,6127,5668,6394,6209,7229,14153,14198],
    type: 'bar'
  }];

  var layout3 = {
    title: {
      text:'The Song Bohemian Rhapsody',
      font: {
        family: 'Courier New, monospace',
        size: 24
      },
    },
    xaxis: {
      title: {
        text: 'month of the year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'sum of the number of plays',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    }
  };

  Plotly.newPlot('myDiv3', data3, layout3, {}, {showSendToCloud:true});

  var data4 = [{
    x: ['January', 'February', 'March', "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    y: [28367,29428,33491,29877,32647,32579,29777,32917,30202,32049,28848,33600],
    type: 'bar'
  }];

  var layout4 = {
    title: {
      text:'Van Halen',
      font: {
        family: 'Courier New, monospace',
        size: 24
      },
    },
    xaxis: {
      title: {
        text: 'month of the year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'sum of the number of plays',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    }
  };

  Plotly.newPlot('VH', data4, layout4, {}, {showSendToCloud:true});

  var data5 = [{
    x: ['January', 'February', 'March', "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    y: [7800,7468,8213,10077,10792,9368,8294,8535,7503,7381,6238,7582],
    type: 'bar'
  }];

  var layout5 = {
    title: {
      text:'Avicii',
      font: {
        family: 'Courier New, monospace',
        size: 24
      },
    },
    xaxis: {
      title: {
        text: 'month of the year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'sum of the number of plays',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    }
  };
  

  Plotly.newPlot('Avicii', data5, layout5, {}, {showSendToCloud:true});

  var data6 = [{
    x: ['January', 'February', 'March', "April", "May", "June", "July", "August", "September", "October", "November", "December"],
    y: [7143, 7190,8008,7208,7711,7338,6687,39107,18356,11333 ,8640,9149],
    type: 'bar'
  }];

  var layout6 = {
    title: {
      text:'Aretha Franklin',
      font: {
        family: 'Courier New, monospace',
        size: 24
      },
    },
    xaxis: {
      title: {
        text: 'month of the year',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      },
    },
    yaxis: {
      title: {
        text: 'sum of the number of plays',
        font: {
          family: 'Courier New, monospace',
          size: 18,
          color: '#7f7f7f'
        }
      }
    }
  };
  

  Plotly.newPlot('Aretha', data6, layout6, {}, {showSendToCloud:true});

  