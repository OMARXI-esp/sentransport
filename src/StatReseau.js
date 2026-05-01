function StatReseau({ lignes }) {
  const totalLignes = lignes.length;

  const totalArrets = lignes.reduce((sum, ligne) => sum + ligne.arrets, 0);

  const maxLigne = lignes.reduce((max, ligne) =>
    ligne.arrets > max.arrets ? ligne : max
  );

  return (
    <div>
      <h3>Statistiques</h3>
      <p>Total lignes : {totalLignes}</p>
      <p>Total arrêts : {totalArrets}</p>
      <p>Ligne ayant le plus d'arrêts : {maxLigne.numero} ({maxLigne.arrets} arrêts)</p>
    </div>
  );
}

export default StatReseau;