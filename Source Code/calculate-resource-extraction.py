(defun calculate-resource-extraction (extraterrestrial-bodies)
  "Calculates the amount of resources extracted from extraterrestrial bodies."
  (let ((total-resources 0))
    (dolist (body extraterrestrial-bodies)
      (let ((resources-extracted (getf body :resources-extracted)))
        (when resources-extracted
          (incf total-resources resources-extracted))
        (let ((children (getf body :children)))
          (when children
            (incf total-resources (calculate-resource-extraction children))))
      (let ((siblings (getf body :siblings)))
        (when siblings
          (incf total-resources (calculate-resource-extraction siblings))))
    total-resources))
